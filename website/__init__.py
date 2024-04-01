from flask import Flask
from website import views
from website import auth
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "user_database.db"

def create_app(database_uri=f"sqlite:///{DB_NAME}"):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ourgreenspace2024"

    # Configure user database 
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri


    db.init_app(app)

    app.register_blueprint(views.views)
    app.register_blueprint(auth.auth)

    from .models import User 

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')