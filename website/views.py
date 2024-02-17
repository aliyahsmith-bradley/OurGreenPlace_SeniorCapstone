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

@views.route("/statistics")
def statistics():
    return render_template("views/statistics.html")

@views.route("/featuredContent")
def featuredContent():
    return render_template("views/featuredContent.html")

@views.route("/howToHelp")
def howToHelp():
    return render_template("views/howToHelp.html")

@views.route("/contact")
def contact():
    return render_template("views/contact.html")