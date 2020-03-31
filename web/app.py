from flask import Flask
import os
from dotenv import load_dotenv
from main import create_app

load_dotenv()

app = Flask(__name__)

apps = create_app()
apps.app_context().push()

if __name__ == '__main__':
    app.run(debug = True, port = os.getenv("PORT"))


