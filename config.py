import os


class Config:
    DEBUG = True

    # db
    SQLALCHEMY_DATABASE_URI = 'postgresql://app:devpass@db:5432/app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # form
    SECRET_KEY = os.environ.get('SECRET_KEY') or "this-is-a-secret"
