from flask import Blueprint, render_template, request, redirect, session
from website.searchGreenSpaces import retrieve_green_spaces, create_green_space_map
from flask_login import current_user 

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("views/home.html", user=current_user)

@views.route("/explore")
def explore():
    green_spaces, city = retrieve_green_spaces()
    return render_template("views/explore.html", green_spaces=green_spaces, city=city, user=current_user)

@views.route("/map")
def map():
    green_spaces, city = retrieve_green_spaces()
    green_space_map = create_green_space_map(green_spaces)
    return render_template("views/map.html", green_space_map=green_space_map, green_spaces=green_spaces, city=city, user=current_user)

@views.route("/deforestationInMD")
def deforestationInMD():
    return render_template("views/deforestationInMD.html", user=current_user)

@views.route("/statistics")
def statistics():
    return render_template("views/statistics.html", user=current_user)

@views.route("/featuredContent")
def featuredContent():
    return render_template("views/featuredContent.html", user=current_user)

@views.route("/howToHelp")
def howToHelp():
    return render_template("views/howToHelp.html", user=current_user)

@views.route("/contact")
def contact():
    return render_template("views/contact.html", user=current_user)