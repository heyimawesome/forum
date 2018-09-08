from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    #app.config.from_pyfile('settings.py', silent=True)

    extensions(app)    
    
    @app.route('/')
    def index():
        return "Hello World!"

    return app

def extensions(app):
    db.init_app(app)