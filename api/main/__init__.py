import os
from flask import Flask
from dotenv import load_dotenv
import main.resources as resources
from flask_restful import Api

api = Api()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    api.add_resources(resources.VerifiedSeisms1Resource, 'Verified-Seisms')
    api.add_resources(resources.VerifiedSeismsResource, '/Verified-Seisms/<id>')
    api.add_resources(resources.UnverifiedSeisms1Resource, 'Unverified-Seism')
    api.add_resources(resources.UnverifiedSeismsResource, 'Unverified-Seisms/<id>')

    api.init_app(app)

    return app
