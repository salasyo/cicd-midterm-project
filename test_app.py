import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_health_route(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_version_route(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert response.get_json()["version"] == "0.1.0"
