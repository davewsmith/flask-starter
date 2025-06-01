from logging.config import dictConfig

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config


db = SQLAlchemy()


def create_app(config_class=Config):
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '%(levelname)s %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

    app = Flask(__name__)
    app.logger.info('made an app')
    app.config.from_object(config_class)

    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        from sqlalchemy import event  # noqa
        from sqlalchemy.engine import Engine  # noqa

        @event.listens_for(Engine, 'connect')
        def _sqlite_pragma(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA journal_mode=WAL;")
            cursor.execute("PRAGMA foreign_keys=ON;")
            cursor.close()

    from app.main import bp as main_bp  # noqa
    app.register_blueprint(main_bp)

    return app
