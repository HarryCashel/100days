import requests
import urllib3
from dateutil.parser import isoparse
import time as t
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://api.sunrise-sunset.org/json"

MY_LAT = -33.831830
MY_LNG = 151.214243

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


def datetime_from_utc_to_local(utc_datetime):
    now_time = t.time()
    offset = datetime.fromtimestamp(now_time) - datetime.utcfromtimestamp(now_time)
    return utc_datetime + offset


response = requests.get(url=url, params=parameters, verify=False)
response.raise_for_status()

data = response.json()

utc_sunset = isoparse(data["results"]["sunset"])
utc_sunrise = isoparse(data["results"]["sunrise"])

datetime_sunset = datetime_from_utc_to_local(utc_sunset)
datetime_sunrise = datetime_from_utc_to_local(utc_sunrise)
print(data)
print(utc_sunset)

print(datetime_sunset)
print(datetime_sunrise)

# date = datetime.today().date()
# print(date)
#
# utc_sunset = datetime.strptime(utc_sunset, f"%H:%M:%S %p")
# print(utc_sunset)
