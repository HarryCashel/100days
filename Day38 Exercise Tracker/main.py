import requests
from datetime import datetime
import os

today = datetime.today().strftime('%d/%m/%Y')
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

TRACK_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]

GOOGLE_API = os.environ["GOOGLE_API"]


def test_endpoint():
    exercise = input("What exercise? ")

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Authorization": f"Basic {AUTH_TOKEN}"
    }
    params = {
        "query": exercise,
        "gender": "male",
        "weight_kg": 65,
        "height_cm": 169,
        "age": 27,
    }

    response = requests.post(url=TRACK_URL, headers=headers, json=params)
    response.raise_for_status()

    return response.json()


data = test_endpoint()["exercises"]


def post_to_sheet():
    for exercise in data:
        workout_data = {
            "workout": {
                "date": today,
                "time": current_time,
                "exercise": exercise["user_input"].title(),
                "duration": f"{(exercise['duration_min'])} min",
                "calories": exercise["nf_calories"]
            }
        }
        response = requests.post(GOOGLE_API, json=workout_data)
        response.raise_for_status()

        print(response.text)


post_to_sheet()
