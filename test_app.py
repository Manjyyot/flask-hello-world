import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World! Welcome to the Flask API." in response.data

def test_hello_world(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_hello_name(client):
    response = client.get('/hello/John')
    assert response.status_code == 200
    assert b"Hello, John!" in response.data
