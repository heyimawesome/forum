from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    pass_hash = db.Column(db.String(128))
    email = db.Column(db.String(128), index=True, unique=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.pass_hash - generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pass_hash, password)
