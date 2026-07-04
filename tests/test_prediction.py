from app.models.predictor import TopicPredictor

predictor = TopicPredictor()


def test_prediction():

    result = predictor.predict(
        "NASA launched a rocket into space."
    )

    assert result["topic"] is not None

    assert result["confidence"] > 0