from flask import Flask
from website import views


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ourgreenspace2024"

    app.register_blueprint(views.views)

    return app