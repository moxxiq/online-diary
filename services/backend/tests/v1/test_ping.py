from starlette.testclient import TestClient

from app.main import v1

client = TestClient(v1)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
