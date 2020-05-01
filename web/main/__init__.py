import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

api = Api()

def create_app():
    app = Flask(__name__)
    load_dotenv()
    #Creación de archivo en base de datos (para SQLite)
    if not os.path.exists(os.getenv('SQLALCHEMY_DATABASE_PATH') + os.getenv('SQLALCHEMY_DATABASE_NAME')):
        os.mknod(os.getenv('SQLALCHEMY_DATEBASE_PATH') + os.getenv('SQLALCHEMY_DATABASE_NAME'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #URL CONFIG.BASE DE DATOS
    app.config['SQLALCHEMY_DATEBASE_URL'] = 'sqlite:////' + os.getenv('SQLALCHEMY_DATEBASE_PATH') + os.getenv('SQLALCHEMY_DATABASE_NAME')
    db.init_app(app)
    import main.resources as resources
    api.add_resource(resources.SensorsResource, 'Sensors')
    api.add_resource(resources.SensorResource, '/Sensor/<id_num>')
    api.add_resource(resources.VerifiedSeismsResource, 'Verified-Seisms')
    api.add_resource(resources.VerifiedSeismResource, '/Verified-Seism/<id_num>')
    api.add_resource(resources.UnverifiedSeismsResource, 'Unverified-Seism')
    api.add_resource(resources.UnverifiedSeismResource, 'Unverified-Seism/<id_num>')
    api.init_app(app)

    return app
