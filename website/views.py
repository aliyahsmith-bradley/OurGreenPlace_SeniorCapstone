from flask import Blueprint, render_template, request
from website.searchGreenSpaces import get_green_spaces as search_green_spaces 

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("views/home.html")

@views.route("/explore")
def show_green_spaces():
    city = request.args.get("city")
    response = search_green_spaces(city)

    #List to store green spaces 
    green_spaces = [] 

    for place_id, green_space_data in response.items():
        # Only include green spaces that are in Maryland 
        if green_space_data.get("state") == "Maryland":
            
            activity_type_name = None

            for activity_type in green_space_data.get("activities", {}):
                # Extract activity type name if found
                activity_type_name = green_space_data["activities"][activity_type].get("activity_type_name")
                if activity_type_name is not None:
                    activity_type_name = activity_type_name.title()
                else:
                    activity_type_name = " " 

            green_space_info = {
                "green_space_id": place_id, 
                "name": green_space_data.get("name", " "),
                "city": green_space_data.get("city", " "), 
                "state": green_space_data.get("state", " "),
                "country": green_space_data.get("country", " "),
                "description": green_space_data.get("description", " "),
                "directions": green_space_data.get("directions", " "),
                "activity_type_name": activity_type_name or "None" # Defaults to "None" if not found
            }

            green_spaces.append(green_space_info)

    return render_template("views/explore.html", green_spaces=green_spaces)

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

@views.route("/signup")
def signup():
    return render_template("views/signup.html")