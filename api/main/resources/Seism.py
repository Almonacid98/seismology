from flask_restful import Resource
from flask import request, jsonify

from main import db
from main.models import SeismModel

class VerifiedSeism(Resource):
    def get(self, id):
        verifiedseism = db.session.query(SeismModel).get_or_404(id)
        return verifiedseism.to_json()

class VerifiedSeisms(Resource):
    def getreturn(self):
        verifiedseisms = db.session.query(SeismModel).all()
        return jsonify({'verifiedseisms': [verifiedseisms.to_json() for verifiedseisms in verifiedseisms]})



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
    def getreturn(self):
        unverifiedseisms = db.session.query(SeismModel).all()
        return jsonify({'unverifiedseisms': [unverifiedseisms.to_json() for unverifiedseisms in unverifiedseisms]})
