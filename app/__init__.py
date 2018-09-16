from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    db.init_app(app)

    from app.auth import bp as bp_auth
    app.register_blueprint(bp_auth, url_prefix='/auth')

    @app.route('/')
    def index():
        return "Hello World!"

    return app
