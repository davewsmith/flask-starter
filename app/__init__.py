from logging.config import dictConfig

from flask import Flask

from config import Config

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

    from app.main import bp as main_bp  # noqa
    app.register_blueprint(main_bp)

    return app

