# From https://flask.palletsprojects.com/en/stable/testing/

import pytest

from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = 1
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


@pytest.fixture()
def flask_app():
    flask_app = create_app(TestConfig)
    yield flask_app


@pytest.fixture()
def client(flask_app):
    return flask_app.test_client()


@pytest.fixture()
def runner(flask_app):
    return flask_app.test_cli_runner()
