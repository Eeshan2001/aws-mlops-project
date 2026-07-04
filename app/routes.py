from flask import Blueprint
from flask import jsonify
from flask import request

from app.inference import predictor
from app.logger import logger
from app.exception import TopicModelException

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():

    return jsonify(
        {
            "project": "Topic Modeling MLOps",
            "status": "Running",
            "version": "1.0"
        }
    )


@main.route("/health", methods=["GET"])
def health():

    return jsonify(
        {
            "status": "healthy"
        }
    )


@main.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        if data is None:

            raise TopicModelException(
                "JSON body not found."
            )

        if "text" not in data:

            raise TopicModelException(
                "'text' field is required."
            )

        text = data["text"]

        if len(text.strip()) == 0:

            raise TopicModelException(
                "Input text cannot be empty."
            )

        result = predictor.predict(text)

        logger.info(
            f"Prediction completed: {result}"
        )

        return jsonify(result)

    except Exception as e:

        logger.exception(str(e))

        return jsonify(
            {
                "error": str(e)
            }
        ), 400