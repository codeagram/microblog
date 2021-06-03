import os


basedir = os.path.abspath(os.path.dirname(__name__))


class Config:

    SECRET_KEY = os.urandom(64)
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{basedir}/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
