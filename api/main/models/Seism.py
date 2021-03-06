from main import db
import datetime as dt
from main.models.Sensor import Sensor
class Seism(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    datetime = db.Column(db.DateTime, nullable=False)
    depth = db.Column(db.Integer, nullable=False)
    magnitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.String, nullable=False)
    longitude = db.Column(db.String, nullable=False)
    verified = db.Column(db.Boolean, nullable=False)
    sensorid = db.Column(db.Integer, db.ForeignKey('sensor.id', ondelete="RESTRICT"), nullable=False)
    sensors = db.relationship("Sensor", back_populates = 'seism', uselist = False, passive_deletes = "all", single_parent = True)
    def __repr__(self):
        return '<Seism %r %r %r' % (self.magnitude, self.latitude, self.longitude)

    def to_json(self):
        self.sensors = db.session.query(Sensor).get(self.sensorid)
        seism_json = {
            'id' : self.id,
            'datetime' : self.datetime.isoformat(),
            'depth' : self.depth,
            'magnitude' : self.magnitude,
            'latitude' : self.latitude,
            'longitude' : self.longitude,
            'verified' : self.verified,
            'sensor' : self.sensors.to_json()

        }
        return seism_json
    @staticmethod
    def from_json(seism_json):
        datetime = dt.datetime.strptime(seism_json.get('datetime'), "%Y-%m-%dT%H:%M:%S")
        depth = seism_json.get('depth')
        magnitude = seism_json.get('magnitude')
        latitude = seism_json.get('latitude')
        longitude = seism_json.get('longitude')
        verified = seism_json.get('verified')
        sensorid = seism_json.get('sensorid')
        return Seism(datetime = datetime,
                     depth = depth,
                     magnitude = magnitude,
                     latitude = latitude,
                     longitude = longitude,
                     verified = verified,
                     sensorid = sensorid
                     )
