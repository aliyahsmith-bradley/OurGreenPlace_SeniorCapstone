from . import db 

class GreenSpace(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    description = db.Column(db.String(500))
    directions = db.Column(db.String(500))
    lat = db.Column(db.Integer)
    lon = db.Column(db.Integer)
    activity_type_name = db.Column(db.String(50))
    length = db.Column(db.String(4))
    rating = db.Column(db.String(4)) 

"""
green_space_info = {
    "green_space_id": place_id, 
    "name": name,
    "city": green_space_data.get("city", " "), 
    "state": green_space_data.get("state", " "),
    # "country": green_space_data.get("country", " "),
    "description": green_space_data.get("description", " "),
    "directions": green_space_data.get("directions", " "),
    "lat": lat,
    "lon": lon,
    "activity_type_name": activity_type_name, # Type of activity (i.e. hiking, mountain biking, etc.)
    "length":length, 
    "rating":rating
    #"thumbnail":thumbnail
}
"""