import requests


API_KEY = "b67aa4f693e4c12d819030c55159ee24"
URL = "http://api.openweathermap.org/data/2.5/onecall"
MY_LAT = -33.831830
MY_LNG = 151.214243


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

for code in hourly_weather_codes:
    if code < 700 and hourly_weather_codes.index(code) == 0:
        print(f"It is raining")
        will_rain = True
    elif code < 700:
        print(f"It is raining in {hourly_weather_codes.index(code)} hours")
        will_rain = True





