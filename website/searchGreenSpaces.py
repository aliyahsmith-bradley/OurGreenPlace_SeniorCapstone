from dotenv import load_dotenv
from pprint import pprint
import requests
import os 

load_dotenv()

def get_green_spaces(city="Baltimore"):
    request_url = "https://trailapi-trailapi.p.rapidapi.com/activity/"

    # Query contains multiple fixed elements (e.g the activity will always be "hiking" currently)
    querystring = {"limit":"25","q-city_cont":{city},"q-country_cont":"United States"}
    
    headers = {
	    "X-RapidAPI-Key": "8a3b9254b6msh07f124103c9bc73p1948dbjsn40b20eb8f6d1",
	    "X-RapidAPI-Host": "trailapi-trailapi.p.rapidapi.com"
    }

    response = requests.get(request_url, headers=headers, params=querystring)

    # for testing purposes -- should output json file in terminal 
    if response.status_code == 200:
        if response.json(): #Check if response is not empty 
            print("\n")
            pprint(response.json())
        else:
            print("No data returned")
    else:
        print(f"Error: {response.status_code}")

    return response.json()
