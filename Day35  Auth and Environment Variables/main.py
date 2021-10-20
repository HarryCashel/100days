import requests
import os
from twilio.rest import Client


API_KEY = os.environ["WEATHER_API_KEY"]
URL = "http://api.openweathermap.org/data/2.5/onecall"
MY_LAT = -33.762232
MY_LNG = 151.123619

TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_TOKEN = os.environ["TWILIO_TOKEN"]
TWILIO_PH_NUM = "+18575778643"
MY_NUM = os.environ["MY_NUM"]

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY
}
response = requests.get(URL, params=parameters)
response.raise_for_status()

data = response.json()
current_temp = data["current"]["temp"]


next_twelve_hour = data["hourly"][:12]

# 0-th index is current hour
hourly_weather_conds = [i["weather"][0]["description"] for i in next_twelve_hour]
hourly_weather_codes = [i["weather"][0]["id"] for i in next_twelve_hour]

print(hourly_weather_conds)
print(hourly_weather_codes)


will_rain = False
message = ""
for code in hourly_weather_codes:
    if code < 700 and hourly_weather_codes.index(code) == 0:
        will_rain = True
        message = "It is raining"
    elif code < 700:
        message = f"It is raining in {hourly_weather_codes.index(code)} hours"
        will_rain = True

if will_rain:

    client = Client(TWILIO_SID, TWILIO_TOKEN)
    message = client.messages \
                    .create(
                         body=message,
                         from_=TWILIO_PH_NUM,
                         to=MY_NUM
                     )

    print(message.status)





