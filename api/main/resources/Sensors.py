from flask_restful import Resource
from flask import request, jsonify

from main import db
from main.models import SensorModel


class Sensor(Resource):

    def get(self, id):
        sensor = db.session.query(SensorModel).get_or_404(id)
        return sensor.to_json()

    def put(self, id):
        sensor = db.session.query(SensorModel).get(id)
        data = request.get_json().items()
        for key, value, in data:
            setattr(sensor, key, value)
        db.session.add(sensor)
        db.session.commit()
        return sensor.to_json(), 201

    def delete(self, id):
        sensor = db.session.query(SensorModel).get_or_404(id)
        db.session.delete(sensor)
        try:
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return '', 409
        return '', 204

class Sensors(Resource):

    #obtener lista de recursos
    def get(self):
        filters = request.get_json().items()
        sensors = db.session.query(SensorModel)
        for key, value in filters:
            if key == 'userid':
                sensors = sensors.filter(SensorModel.userid == value)
            if key == 'port':
                sensors = sensors.filter(SensorModel.port == value)
            if key == "status":
                sensors = sensors.filter(SensorModel.status == value)
            if key == "active":
                sensors = sensors.filter(SensorModel.active == value)

        sensors.all()
        return jsonify ({'sensors' : [sensor.to_json() for sensor in sensors]})
    #insertar recurso

    def post(self):
        sensor = SensorModel.from_json(request.get_json())
        db.session.add(sensor)
        db.session.commit()
        return sensor.to_json(), 201
