from fastapi.testclient import TestClient

from app.app import app

client = TestClient(app)


def test_predict_spam():
    response = client.post(
        "/api/predict",
        json={
            "email_text": """
            Subject: Congratulations!

            You have won a $1000 Amazon gift card.
            Click here to claim your prize.
            """
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "confidence" in data

    assert data["prediction"] in ("spam", "ham")
    assert isinstance(data["confidence"], float)
    assert 0.0 <= data["confidence"] <= 1.0


def test_predict_ham():
    response = client.post(
        "/api/predict",
        json={
            "email_text": """
            Subject: Project Meeting

            Hi Team,

            The meeting is tomorrow at 10 AM.

            Regards,
            John
            """
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "confidence" in data

    assert data["prediction"] in ("spam", "ham")
    assert isinstance(data["confidence"], float)
    assert 0.0 <= data["confidence"] <= 1.0