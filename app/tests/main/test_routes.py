from http import HTTPStatus

import pytest


def test_home(client):
    response = client.get("/")
    assert HTTPStatus.OK == response.status_code


def test_fail(client):
    with pytest.raises(Exception):
        client.get("/fail")
