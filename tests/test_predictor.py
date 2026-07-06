from app.predictor import predict_spam


def test_predict_spam():
    email = """
    Subject: Congratulations!

    You have won a $1000 Amazon gift card.
    Click the link below to claim your prize now.
    """

    prediction, confidence = predict_spam(email)
    print(prediction)
    print(confidence)
    assert prediction == "spam"
    assert isinstance(confidence, float)
    assert 0.0 <= confidence <= 1.0


def test_predict_ham():
    email = """
    Subject: Project Meeting

    Hi Team,

    The project meeting has been scheduled for tomorrow at 10:00 AM.
    Please bring the updated presentation.

    Regards,
    John
    """

    prediction, confidence = predict_spam(email)
    print(prediction)
    print(confidence)
    assert prediction == "ham"
    assert isinstance(confidence, float)
    assert 0.0 <= confidence <= 1.0