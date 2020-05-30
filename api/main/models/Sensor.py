from main import db
from main.models.User import User
class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    ip = db.Column(db.String(100), nullable = False)
    port = db.Column(db.Integer, nullable = False)
    status = db.Column(db.Boolean, nullable = False)
    active = db.Column(db.Boolean, nullable = False)
    userid = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    seism = db.relationship("Seism", back_populates = 'sensors', passive_deletes = "all", single_parent = True)
    user = db.relationship("User", back_populates = 'sensor', uselist = False, single_parent = True)
    def __repr__(self):
        return '<Sensor %r >' % (self.name)

    def to_json(self):
        self.user = db.session.query(User).get(self.userid)
        print(self.user)
        try:
            sensor_json = {
                'id': self.id,
                'name': str(self.name),
                'ip': str(self.ip),
                'port': self.port,
                'status': self.status,
                'active': self.active,
                'user': self.user.to_json()
            }
        except AttributeError:
            sensor_json = {
                'id': self.id,
                'name': str(self.name),
                'ip': str(self.ip),
                'port': self.port,
                'status': self.status,
                'active': self.active,
                'userid': self.userid
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