from flask import Blueprint, render_template, request
from website.searchGreenSpaces import retrieve_green_spaces
from flask_login import current_user 
import folium

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("views/home.html", user=current_user)

@views.route("/explore")
def explore():
    green_spaces = retrieve_green_spaces()
    return render_template("views/explore.html", green_spaces=green_spaces, user=current_user)

@views.route("/map")
def map():
    green_spaces = retrieve_green_spaces()

    # Coordinates are center of Maryland 
    green_space_map = folium.Map(location=[39.0458, -76.6413], zoom_start=9)

    # Adds marker on map for each green space in Maryland -- need specific city to display 
    for green_space in green_spaces:
        lat = float(green_space["lat"]) 
        lon = float(green_space["lon"])  
        coords = (lat, lon) 
        folium.Marker(coords).add_to(green_space_map)

    green_space_map = green_space_map._repr_html_()

    return render_template("views/map.html", green_space_map=green_space_map, green_spaces=green_spaces, user=current_user)

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