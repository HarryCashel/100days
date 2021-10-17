import requests
import json

response = requests.get("http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data = response.json()

current_latitude = data["iss_position"]["latitude"]
current_longitude = data["iss_position"]["longitude"]

iss_position = (current_latitude, current_longitude)
