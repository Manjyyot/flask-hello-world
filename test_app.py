import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello world with Flask" in response.data

def test_not_found(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
