from flask import Flask
from website import views
from website import auth
from flask_sqlalchemy import SQLAlchemy 
from os import path

db = SQLAlchemy()
DB_NAME = "user_database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ourgreenspace2024"

    # Configure user database 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views.views)
    app.register_blueprint(auth.auth)

    from .models import User 

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')