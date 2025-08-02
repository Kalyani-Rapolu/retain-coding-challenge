import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"

def test_shorten_and_redirect(client):
    res = client.post("/api/shorten", json={"url": "https://example.com"})
    assert res.status_code == 201
    data = res.get_json()
    short_code = data["short_code"]

    res2 = client.get(f"/{short_code}")
    assert res2.status_code == 302

    res3 = client.get(f"/api/stats/{short_code}")
    assert res3.status_code == 200
    assert res3.get_json()["clicks"] >= 1
