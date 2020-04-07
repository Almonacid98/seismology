from flask_restful import Resource
from flask import request
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
        if int(id) in SENSORS:
            return SENSORS[int(id)]
        return '', 404
    def put(self, id):
        if int(id) in SENSORS:
            sensor = SENSORS[int(id)]
            data = request.get_json()
            sensor.update(data)
            return sensor, 201
        return '', 404
    def delete(self, id):
        if int(id) in SENSORS:
            del SENSORS[int(id)]
            return '', 204
        return '', 404

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
