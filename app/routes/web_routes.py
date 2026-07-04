from flask import Blueprint
from flask import render_template
from flask import request

from app.services.prediction_service import PredictionService

web = Blueprint(
    "web",
    __name__
)


@web.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    confidence = None

    error = None

    if request.method == "POST":

        try:

            result = PredictionService.predict(

                request.form["text"]

            )

            prediction = result["topic"]

            confidence = result["confidence"]

        except Exception as ex:

            error = str(ex)

    return render_template(

        "index.html",

        prediction=prediction,

        confidence=confidence,

        error=error

    )