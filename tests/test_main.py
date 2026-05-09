import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Enter your name" in response.data


def test_home_post(client):
    response = client.post("/", data={"name": "Alice"})
    assert response.status_code == 200
    assert b"Alice" in response.data


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"