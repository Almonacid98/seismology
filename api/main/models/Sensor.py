from main import db
from main.models import UserModel
class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    ip = db.Column(db.String(100), nullable = False)
    port = db.Column(db.Integer, nullable = False)
    status = db.Column(db.Boolean, nullable = False)
    active = db.Column(db.Boolean, nullable = False)
    userid = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    seism = db.relationship("Seism", back_populate = 'sensors', passive_delete = "all", single_parent = True)
    user = db.relationship("User", back_populate = 'sensor', uselist = False, single_parent = True)
    def __repr__(self):
        return '<Sensor %r >' % (self.name)

    def to_json(self):
        self.user = db.session.query(UserModel).get_or_404(self.userid)
        sensor_json = {
            'id' : self.id,
            'name' : str(self.name),
            'ip' : str(self.ip),
            'port' : self.port,
            'status' : self.status,
            'active' : self.active,
            'user' : self.user.to_json()
        }
        return sensor_json
    @staticmethod
    def from_json(sensor_json):
        name = sensor_json.get('name')
        ip = sensor_json.get('ip')
        port = sensor_json.get('port')
        status = sensor_json.get('status')
        active = sensor_json.get('active')
        userid = sensor_json.get('userid')
        return Sensor(
            name = name,
            ip = ip,
            port = port,
            status = status,
            active = active,
            userid = userid
        )