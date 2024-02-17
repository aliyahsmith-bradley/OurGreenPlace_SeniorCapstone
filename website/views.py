from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("views/home.html")

@views.route("/explore")
def explore():
    return render_template("views/explore.html")

@views.route("/deforestationInMD")
def deforestationInMD():
    return render_template("views/deforestationInMD.html")

@views.route("/contact")
def contact():
    return render_template("views/contact.html")