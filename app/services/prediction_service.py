from app.utils.validators import InputValidator
from app.extensions import predictor


class PredictionService:

    @staticmethod
    def predict(text):

        validated_text = InputValidator.validate_text(text)

        return predictor.predict(validated_text)