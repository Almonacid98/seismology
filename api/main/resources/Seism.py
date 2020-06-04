from flask_restful import Resource
from flask import request, jsonify
from random import randint, uniform
from datetime import datetime
from main import db
from main.models import SeismModel

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
                verifiedseisms = verifiedseisms.filter(SeismModel.datetime.like("%" + str(value) + "%"))
            if key == 'magnitude':
                verifiedseisms = verifiedseisms.filter(SeismModel.magnitude.like("%" + str(value) + "%"))
    
        return jsonify({'verifiedseisms': [verifiedseisms.to_json() for verifiedseisms in verifiedseisms]})

    def post(self):
        seismnew = SeismModel(
            datetime=datetime(
                randint(1965, 2019),
                randint(1, 12),
                randint(1, 28),
                randint(00, 23),
                randint(0, 59),
                randint(0, 59)
            ),
            depth=randint(5, 250),
            magnitude=round(uniform(2.0, 5.5), 1),
            latitude=uniform(-180, 180),
            longitude=uniform(-90, 90),
            verified=True
            )
        db.session.add(seismnew)
        db.session.commit()
        return seismnew.to_json(), 201


class UnverifiedSeism(Resource):
    def get(self, id):
        unverifiedseism = db.session.query(SeismModel).get_or_404(id)
        return unverifiedseism.to_json()
    def put(self, id):
        unverifiedseism = db.session.query(SeismModel).get(id)
        data = request.get_json().items()
        for key, value, in data:
            setattr(unverifiedseism, key, value)
        db.session.add(unverifiedseism)
        db.session.commit()
        return unverifiedseism.to_json(), 201
    def delete(self, id):
        unverifiedseism = db.session.query(SeismModel).get_or_404(id)
        db.session.delete(unverifiedseism)
        db.session.commit()
        return '', 404


class UnverifiedSeisms(Resource):
    def get(self):
        filters = request.get_json().items()

        unverifiedseisms = db.session.query(SeismModel).filter(SeismModel.verified == True)
        for (key, value) in filters:
            if key == 'datetime':
                unverifiedseisms = unverifiedseisms.filter(SeismModel.datetime.like("%" + str(value) + "%"))
            if key == 'magnitude':
                unverifiedseisms = unverifiedseisms.filter(SeismModel.magnitude.like("%" + str(value) + "%"))
    

        return jsonify({'unverifiedseisms': [unverifiedseisms.to_json() for unverifiedseisms in unverifiedseisms]})

    def post(self):
        seismnew = SeismModel(
            datetime=datetime(
                randint(1965, 2019),
                randint(1, 12),
                randint(1, 28),
                randint(00, 23),
                randint(0, 59),
                randint(0, 59)
            ),
            depth=randint(5, 250),
            magnitude=round(uniform(2.0, 5.5), 1),
            latitude=uniform(-180, 180),
            longitude=uniform(-90, 90),
            verified=False,
            sensorid = randint(0, 5)
            )
        db.session.add(seismnew)
        db.session.commit()
        return seismnew.to_json(), 201
