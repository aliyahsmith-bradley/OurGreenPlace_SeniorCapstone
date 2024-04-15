from flask import Flask
from website import views
from website import auth
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
USER_DB = "user_database.db"
GREEN_SPACE_DB = "greenSpace_database.db"

def create_app(user_database_uri=f"sqlite:///{USER_DB}", greenSpace_database_uri=f"sqlite:///{GREEN_SPACE_DB}"):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ourgreenspace2024"

    # Configure user database 
    app.config['SQLALCHEMY_DATABASE_URI'] = user_database_uri

    db.init_app(app)

    app.register_blueprint(views.views)
    app.register_blueprint(auth.auth)

    from .userModels import User 

    create_database(app, USER_DB)

    # Create green space database 
    app.config['SQLALCHEMY_DATABASE_URI'] = greenSpace_database_uri
    from .greenSpaceModels import GreenSpace 
    create_database(app, GREEN_SPACE_DB)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app, database):
    if not path.exists('website/' + database):
        with app.app_context():
            db.create_all()
            print('Created Database!')