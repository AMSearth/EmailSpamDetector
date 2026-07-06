from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app=app)


def test_root():
    res = client.get("/")
    assert res.status_code == 200