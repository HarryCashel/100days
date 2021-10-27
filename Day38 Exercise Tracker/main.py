import requests
from datetime import datetime
import os

today = datetime.today().strftime('%Y%m%d')

TRACK_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]

GOOGLE_API = os.environ["GOOGLE_API"]


def test_endpoint():
    exercise = input("What exercise? ")

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
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

    return response


print(test_endpoint().text)
