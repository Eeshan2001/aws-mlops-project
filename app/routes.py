from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify(
        {
            "project": "Topic Modeling MLOps",
            "status": "Running",
            "version": "1.0"
        }
    )