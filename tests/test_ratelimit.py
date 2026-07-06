# tests/test_rate_limit.py

from fastapi.testclient import TestClient
from app.app import app
import pytest
from app.rate_limiting import limiter

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_rate_limits():
    limiter._storage.reset()

def test_predict_rate_limit():
    payload = {
        "email_text": "Congratulations! You have won $1000."
    }

    # First 10 requests should succeed
    for _ in range(10):
        response = client.post("/api/predict", json=payload)
        assert response.status_code == 200

    # 11th request should be blocked
    response = client.post("/api/predict", json=payload)

    assert response.status_code == 429