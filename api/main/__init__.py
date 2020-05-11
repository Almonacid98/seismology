import os
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if os.getenv('SQLALCHEMY_DATABASE_TYPE') == 'sqlite':  
    #Creación de archivo en base de datos (para SQLite) Post data: Se agregaron los .db que faltaban
        if not os.path.exists(os.getenv('SQLALCHEMY_DATABASE_PATH') + os.getenv('SQLALCHEMY_DATABASE_NAME')+'.db'):
            os.mknod(os.getenv('SQLALCHEMY_DATABASE_PATH') + os.getenv('SQLALCHEMY_DATABASE_NAME')+'.db')
    #URL CONFIG.BASE DE DATOS (BASE DE DATOS EN SQLITE)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.getenv('SQLALCHEMY_DATABASE_PATH') + os.getenv('SQLALCHEMY_DATABASE_NAME')+'.db'
    
    #URL CONFIG.BASE DE DATOS (BASE DE DATOS MYSQL)

    if os.getenv('SQLALCHEMY_DATABASE_TYPE') == 'mysql':
      app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+os.getenv('SQLALCHEMY_DATABASE_USER')+':'+os.getenv('SQLALCHEMY_DATABASE_PASS')+'@'+os.getenv('SQLALCHEMY_DATABASE_IP')+'/'+os.getenv('SQLALCHEMY_DATABASE_NAME')  
    
    db.init_app(app)

    #verificación de la conexión sqlite
    if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
        def activatePrimaryKeys(conection, conection_record):
            #ejecución del comando (activa claves foraneas en sqlite)
            conection.execute('pragma foreign_keys = ON')
        with app.app_context():
            from sqlalchemy import event
            #al realizar conexión con la base de datos llama a la función que activa las claves foraneas
            event.listen(db.engine, 'connect', activatePrimaryKeys)
            
    import main.resources as resources
    api.add_resource(resources.UsersResource, '/users')
    api.add_resource(resources.UserResource, '/user/<id>')
    api.add_resource(resources.SensorsResource, '/sensors')
    api.add_resource(resources.SensorResource, '/sensor/<id>')
    api.add_resource(resources.VerifiedSeismsResource, '/verified-seisms')
    api.add_resource(resources.VerifiedSeismResource, '/verified-seism/<id>')
    api.add_resource(resources.UnverifiedSeismsResource, '/unverified-seisms')
    api.add_resource(resources.UnverifiedSeismResource, '/unverified-seism/<id>')
    api.init_app(app)
    #Recursos
    return app
