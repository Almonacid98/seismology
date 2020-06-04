from flask_restful import Resource
from flask import request, jsonify
from random import randint, uniform
from datetime import datetime
from main import db
from main.models import SeismModel
from main.models.Sensor import Sensor

class VerifiedSeism(Resource):
    def get(self, id):
        verifiedseism = db.session.query(SeismModel).get_or_404(id)
        return verifiedseism.to_json()

class VerifiedSeisms(Resource):
    def get(self):
        filters = request.get_json().items()
        verifiedseisms = db.session.query(SeismModel).filter(SeismModel.verified == True)
        for (key, value) in filters:
            if key == 'datetime':
                verifiedseisms = verifiedseisms.filter(SeismModel.datetime == value)
            if key == 'magnitude':
                verifiedseisms = verifiedseisms.filter(SeismModel.magnitude == value)
            if key == 'sensorid':
                verifiedseisms = verifiedseisms.filter(SeismModel.sensorid == value)
            if key == 'id':
                verifiedseisms = verifiedseisms.filter(SeismModel.id == value)
            verifiedseisms.all()

        return jsonify({'verifiedseisms': [verifiedseisms.to_json() for verifiedseism in verifiedseisms]})


class UnverifiedSeism(Resource):
    def get(self, id):
        unverifiedseism = db.session.query(SeismModel).get_or_404(id)
        return unverifiedseism.to_json()
    def put(self, id):
        unverifiedseism = db.session.query(SeismModel).get_or_404(id)
        data = request.get_json().items()
        for key, value, in data:
            if key == 'datatime':
                setattr(unverifiedseism, key, datetime.strftime(value, "%Y-%m-%d %H:%M:%S"))
            elif key == 'sensorid':
                a = db.session.query(SensorModel).get(value)
                setattr(unverifiedseism, key, value)
            else:
                setattr(unverifiedseism, key, value)
        db.session.add(unverifiedseism)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            return '', 409
        return unverifiedseism.to_json(), 201
    def delete(self, id):
        unverifiedseism = db.session.query(SeismModel).get_or_404(id)
        db.session.delete(unverifiedseism)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            return '', 409
        return '', 204


class UnverifiedSeisms(Resource):
    def get(self):
        filters = request.get_json().items()
        unverifiedseisms = db.session.query(SeismModel).filter(SeismModel.verified == False)
        for key, value in filters:
            if key == 'id':
                unverifiedseisms = unverifiedseisms.filter(SeismModel.id == value)
            if key == 'datatime':
                unverifiedseisms = unverifiedseisms.filter(SeismModel.datetime == value)
            if key == 'magnitude':
                unverifiedseisms = unverifiedseisms.filter(SeismModel.magnitude == value)
            if key == 'sensorid':
                unverifiedseisms = unverifiedseisms.filter(SeismModel.sensorid == value)
            unverifiedseisms.all()
        return jsonify({'unverifiedseisms': [unverifiedseisms.to_json() for unverifiedseism in unverifiedseisms]})
   