from flask import Flask
from website import views
from website import auth
from flask_sqlalchemy import SQLAlchemy 


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ourgreenspace2024"

    app.register_blueprint(views.views)
    app.register_blueprint(auth.auth)

    return app