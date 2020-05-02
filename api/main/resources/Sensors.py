from flask_restful import Resource
from flask import request, jsonify
from main import db
from main.models import SensorModel
from main.models.User import User as UserModel
SENSORS = {
    1: {'numberS': '0008', 'name': 'Buenos Aires, Argentina', 'status': 'disable'},
    2: {'numberS': '0010', 'name': 'Madrid, España', 'status': 'enabled'},
    3: {'numberS': '0100', 'name': 'Distrito Federal, Mexico ', 'status': 'enabled'},
    4: {'numberS': '0089', 'name': 'Lima, Perú', 'status': 'disabled'},
    5: {'numberS': '0555', 'name': 'San Pablo, Brasil', 'status': 'enabled'},
    6: {'numberS': '0124', 'name': 'Santiago, Chile', 'status': 'enabled'}
}


class Sensor(Resource):
    def get(self, id):
        sensor = db.session.query(SensorModel).get_or_404(id)
        return sensor.to_json()
    def put(self, id):
        sensor = db.session.query(SensorModel).get(id)
        filters = request.get_json().items()
        for key, value in filters:
            if key == 'userid':
                v = db.session.query(UserModel).get_or_404(value)
                setattr(sensor, key, value)
            else:
                setattr(sensor, key, value)
        db.session.add(sensor)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            return '', 409
        return sensor.to_json(), 201
    def delete(self, id):
        sensor = db.session.query(SensorModel).get_or_404(id)
        db.session.delete(sensor)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            return '', 409
        return '', 204


class Sensors(Resource):
    def get(self):
        return SENSORS, 200

    def post(self):
        sensor = request.get_json()
        print(SENSORS.keys())
        print(max(SENSORS.keys()))
        id = int(max(SENSORS.keys())) + 1
        SENSORS[id] = sensor
        return SENSORS[id], 201
