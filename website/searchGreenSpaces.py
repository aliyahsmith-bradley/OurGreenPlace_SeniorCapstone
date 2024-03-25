from dotenv import load_dotenv
from pprint import pprint
from flask import request
import requests, folium

load_dotenv() 

def request_green_spaces(city="Baltimore"): # Baltimore set as default 
    request_url = "https://trailapi-trailapi.p.rapidapi.com/activity/"

    # Query contains multiple fixed elements 
    querystring = {
        "limit":"25",
        "q-city_cont":{city},
        "q-state_cont":"Maryland",
        "q-country_cont":"United States"}
    
    headers = {
	    "X-RapidAPI-Key": "8a3b9254b6msh07f124103c9bc73p1948dbjsn40b20eb8f6d1",
	    "X-RapidAPI-Host": "trailapi-trailapi.p.rapidapi.com"
    }

    response = requests.get(request_url, headers=headers, params=querystring)

     # for testing purposes -- should output json file in terminal 
    """
    if response.status_code == 200:
        if response.json(): #Check if response is not empty 
            print("\n")
            pprint(response.json())
        else:
            print("No data returned")
    else:
        print(f"Error: {response.status_code}")
    """

    return response.json()

def retrieve_green_spaces():
    city = request.args.get("city")
    response = request_green_spaces(city)

    # List to store green spaces 
    green_spaces = []  

    for place_id, green_space_data in response.items():

        # Attributes
        activity_type_name = None
        length = None 
        rating = None
        thumbnail = None 
        lat = green_space_data.get("lat", None)
        lon = green_space_data.get("lon", None)

        for activity_type in green_space_data.get("activities", {}):
            activity_data = green_space_data["activities"][activity_type]

            activity_type_name = activity_data.get("activity_type_name")
            if activity_type_name is not None:
                activity_type_name = activity_type_name.title()
            else:
                activity_type_name = "N/A"
            
            # Extract rating if present, "N/A" if not 
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

        # Fixes bug where there are "None" types in API data 
        # However, now there is a duplicate card being created at the end of the list 
        name = green_space_data.get("name")
        if name is not None:
            green_space_info = {
                "green_space_id": place_id, 
                "name": name,
                "city": green_space_data.get("city", " "), 
                "state": green_space_data.get("state", " "),
                "country": green_space_data.get("country", " "),
                "description": green_space_data.get("description", " "),
                "directions": green_space_data.get("directions", " "),
                "lat": lat,
                "lon": lon,
                "activity_type_name": activity_type_name,
                "length":length, 
                "rating":rating,
                "thumbnail":thumbnail
            }

        green_spaces.append(green_space_info)
    
    # Testing 
    print(green_spaces)
    return green_spaces, city

def create_green_space_map(green_spaces):
    # Coordinates are center of Maryland 
    green_space_map = folium.Map(location=[39.0458, -76.6413], zoom_start=10)

    # Adds marker on map for each green space in Maryland 
    for green_space in green_spaces: 
        coords = (green_space["lat"], green_space["lon"]) 
        popup=(
            "<div style='width: 200px;'>" + 
            "<h3>" + green_space["name"] + "</h3>"
            "<h5>Type: " + green_space["activity_type_name"] + "</h5>"
            "<h5>Length: " + green_space["length"] + "</h5>"
            "<h5>Rating: " + green_space["rating"] + "</h5>" 
            + "<\div>"
        )
        folium.Marker(coords, popup).add_to(green_space_map)

    # Converts map to HTML 
    green_space_map = green_space_map._repr_html_()

    return green_space_map