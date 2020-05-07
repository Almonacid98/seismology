from flask import Flask
import os
from dotenv import load_dotenv
from main import create_app
from main import db
load_dotenv()


app = create_app()
app.app_context().push()

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True, port = os.getenv("PORT"))


