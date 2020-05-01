from .. import db
class Sensor(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    ip = db.Column(db.String(100), nullable = False)
    port = db.Column(db.Integer, primary_key = True)
    status = db.Column(db.boolean, nullable = False)
    active = db.Column(db.boolean, nullable = False)
    userid = db.Column(db.Integer, primary_key = True)
