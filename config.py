import os


basedir = os.path.abspath(os.path.dirname(__file__))
sqlite_db = 'sqlite:///' + os.path.join(basedir, 'data', 'app.db')


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or sqlite_db
