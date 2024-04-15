from . import db 
from flask_login import UserMixin

class User(db.Model, UserMixin): # only use UserMixin for login 
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True) # ensures email must be unique
    username = db.Column(db.String(150), unique=True) 
    password = db.Column(db.String(150))
 