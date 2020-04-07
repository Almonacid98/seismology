import os
from flask import Flask
from dotenv import load_dotenv
import main.resources as resources
from flask_restful import Api

api = Api()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    api.add_resource(resources.SensorsResource, 'Sensors')
    api.add_resource(resources.SensorResource, '/Sensor/<id_num>')
    api.add_resource(resources.VerifiedSeismsResource, 'Verified-Seisms')
    api.add_resource(resources.VerifiedSeismResource, '/Verified-Seism/<id_num>')
    api.add_resource(resources.UnverifiedSeismsResource, 'Unverified-Seism')
    api.add_resource(resources.UnverifiedSeismResource, 'Unverified-Seism/<id_num>')

    api.init_app(app)

    return app
