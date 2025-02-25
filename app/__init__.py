from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        from sqlalchemy import event  # noq
        from sqlalchemy.engine import Engine  # noqa

        @event.listens_for(Engine, 'connect')
        def _sqlite_pragma(dbapi_connection, connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGME foreign_keys=ON;")
            cursor.close()

    migrate.init_app(app, db, render_as_batch=True)

    from app.main import bp as main_bp  # noqa
    app.register_blueprint(main_bp)

    return app
