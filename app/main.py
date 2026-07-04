from flask import Flask

from app.routes.api_routes import api

from app.routes.web_routes import web


def create_app():

    app = Flask(__name__)

    app.register_blueprint(api)

    app.register_blueprint(web)

    return app