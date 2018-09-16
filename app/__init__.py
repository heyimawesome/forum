from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    db.init_app(app)
    login.init_app(app)

    from app.auth import bp as bp_auth
    app.register_blueprint(bp_auth, url_prefix='/auth')

    from app.main import bp as bp_main
    app.register_blueprint(bp_main)

    return app
