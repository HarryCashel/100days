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

next_twelve_hour = data["hourly"][:13]
hourly_weather_cond = [i["weather"][0]["description"] for i in next_twelve_hour]
print(hourly_weather_cond)




