from flask import Blueprint
from flask import jsonify
from flask import request

from app.services.prediction_service import PredictionService

api = Blueprint(
    "api",
    __name__
)


@api.route("/predict", methods=["POST"])
def predict():

    body = request.get_json()

    result = PredictionService.predict(
        body["text"]
    )

    return jsonify(result)


@api.route("/health")
def health():

    return jsonify(

        {

            "status": "healthy"

        }

    )