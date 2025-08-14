import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_user(client):
    res = client.post('/users', json={"name": "Alice", "email": "alice@mail.com"})
    assert res.status_code == 201
    assert res.json['name'] == "Alice"

def test_get_users(client):
    res = client.get('/users')
    assert res.status_code == 200
