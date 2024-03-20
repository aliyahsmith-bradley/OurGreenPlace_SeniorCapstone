from flask import Blueprint, render_template, request
from website.searchGreenSpaces import get_green_spaces as search_green_spaces
from flask_login import login_required, current_user 

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("views/home.html", user=current_user)

@views.route("/explore")
def show_green_spaces():
    city = request.args.get("city")
    response = search_green_spaces(city)

    # List to store green spaces 
    green_spaces = [] 

    for place_id, green_space_data in response.items():
        # Only include green spaces that are in Maryland 
        if green_space_data.get("state") == "Maryland":
            
            activity_type_name = None
            length = None 
            rating = None
            thumbnail = None 

            for activity_type in green_space_data.get("activities", {}):
                activity_data = green_space_data["activities"][activity_type]

                activity_type_name = activity_data.get("activity_type_name")
                if activity_type_name is not None:
                    activity_type_name = activity_type_name.title()
                else:
                    activity_type_name = "N/A"
                
                # Extract rating if present
                rating = activity_data.get("rating")
                if rating is not None and rating != "0.00":
                    rating = str(rating).title() + "/5.00"
                else:
                    rating = "N/A"

            activities = green_space_data.get("activities", {})

            for activity_type, activity_data in activities.items():
                attribs = activity_data.get("attribs", {})
                
                if "length" in attribs:
                    length = attribs["length"]
                    if length is not None and length != "0":
                        length = str(length).title() + " Miles"
                    else:
                        length = "N/A"

                thumbnail = activity_data.get("thumbnail")
                if thumbnail:
                    break  
                else:
                    thumbnail = "/static/images/hiking_trail_image.png"

            green_space_info = {
                "green_space_id": place_id, 
                "name": green_space_data.get("name", " "),
                "city": green_space_data.get("city", " "), 
                "state": green_space_data.get("state", " "),
                "country": green_space_data.get("country", " "),
                "description": green_space_data.get("description", " "),
                "directions": green_space_data.get("directions", " "),
                "activity_type_name": activity_type_name,
                "length":length, 
                "rating":rating,
                "thumbnail":thumbnail
            }

            green_spaces.append(green_space_info)

    return render_template("views/explore.html", green_spaces=green_spaces, user=current_user)

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