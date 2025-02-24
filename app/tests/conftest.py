import pytest

from app import create_app
from config import Config


class TestConfig(Config):
    TESTING = True


@pytest.fixture()
def flask_app():
    app = create_app(TestConfig)
    # setUp TBD
    yield app
    # tearDown TBD


@pytest.fixture()
def client(flask_app):
    return flask_app.test_client()
