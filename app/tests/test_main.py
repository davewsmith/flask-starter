import sqlalchemy as sa

from app import db
from app.main.models import User


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data


def test_user(client):
    user = User(username='test', email='test@example.com')
    db.session.add(user)
    db.session.commit()

    query = sa.select(User)
    users = db.session.scalars(query).all()
    assert len(users) == 1
    assert users[0].username == 'test'
    assert users[0].email == 'test@example.com'
