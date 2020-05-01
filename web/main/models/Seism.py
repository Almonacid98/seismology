from .. import db
class Seism(db.model):
    id = db.Column(db.Integer, primary_key = True)
    datetime =
    depth =
    magnitude =
    latitude =
    longitude =
    verified =
    sensorid =
