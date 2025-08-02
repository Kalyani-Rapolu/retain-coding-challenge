import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get("/")
    assert res.status_code == 200
    assert "User API running" in res.get_json()["status"]

def test_create_user(client):
    res = client.post("/users", json={
        "name": "John Doe",
        "email": "john@example.com",
        "password": "123456"
    })
    assert res.status_code == 201
