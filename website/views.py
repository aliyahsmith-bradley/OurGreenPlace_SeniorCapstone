from flask import Blueprint, render_template, flash, redirect, url_for
from website.searchGreenSpaces import retrieve_green_spaces, create_green_space_map, check_city
from flask_login import current_user, login_required 

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("views/home.html", user=current_user)

@views.route("/explore")
@login_required  
def explore():
    # if check_city():
        # green_spaces, city = retrieve_green_spaces()
        # return render_template("views/explore.html", green_spaces=green_spaces, city=city, user=current_user)
    #else:
        #flash("Please input a city in Maryland.", category='error')
        
    #return redirect(url_for('views.home'))
    green_spaces, city = retrieve_green_spaces()
    return render_template("views/explore.html", green_spaces=green_spaces, city=city, user=current_user)

@views.route("/map")
@login_required
def map():
    green_spaces, city = retrieve_green_spaces()
    green_space_map = create_green_space_map(green_spaces)
    return render_template("views/map.html", green_space_map=green_space_map, green_spaces=green_spaces, city=city, user=current_user)



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

@views.route("/addToDatabase")
def addToDatabase():
    return render_template("views/addToDatabase.html", user=current_user)