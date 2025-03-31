import pytest
from app import app

@pytest.fixture
def client():
    # Set up the Flask test client
    with app.test_client() as client:
        yield client

def test_home(client):
    # Test the home route
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello DevOps, this is David Reporting for duty "