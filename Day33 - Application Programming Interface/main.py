import requests
import urllib3
from dateutil.parser import isoparse
import time as t
from datetime import datetime, timedelta
import smtplib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Constants
MY_LAT = -33.831830
MY_LNG = 151.214243
EMAIL = "cashel.harry101@gmail.com"
PASSWORD = "wy(L*,Yj+F"


def get_current_iss_pos():
    """Gets the current position of the International Space Station"""
    response = requests.get("http://api.open-notify.org/iss-now.json")

    response.raise_for_status()

    data = response.json()

    current_latitude = data["iss_position"]["latitude"]
    current_longitude = data["iss_position"]["longitude"]

    iss_position = (float(current_latitude), float(current_longitude))
    return iss_position


def tuple_diff(iss_pos_tuple, my_pos_tuple):
    """Returns the difference of latitude and longitude"""
    lat_diff = abs(iss_pos_tuple[0] - my_pos_tuple[0])
    lng_diff = abs(iss_pos_tuple[1] - my_pos_tuple[1])
    return round(lat_diff, 6), round(lng_diff, 6)


def viewable_difference(tup):
    """Returns True if the difference is under 5. False otherwise"""
    if tup[0] > 4 and tup[1] > 4:
        return True
    return False


def datetime_from_utc_to_local(utc_datetime):
    """Takes a utc datetime and returns local time"""
    now_time = t.time()
    offset = datetime.fromtimestamp(now_time) - datetime.utcfromtimestamp(now_time)
    return utc_datetime + offset


def get_local_sun():
    """Gets the local sunrise and sunset times"""
    url = "https://api.sunrise-sunset.org/json"

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url=url, params=parameters, verify=False)
    response.raise_for_status()

    data = response.json()

    utc_sunset = isoparse(data["results"]["sunset"])
    utc_sunrise = isoparse(data["results"]["sunrise"])

    datetime_sunset = datetime_from_utc_to_local(utc_sunset)
    datetime_sunrise = datetime_from_utc_to_local(utc_sunrise)
    return datetime_sunrise, datetime_sunset


def is_dark():
    """Check if it is before sunrise or after sunset in current timezone"""
    time_now = datetime.now()
    local_sunrise = get_local_sun()[0]
    local_sunset = get_local_sun()[1]
    if time_now.hour >= local_sunset.hour or time_now.hour <= local_sunrise.hour:
        return True
    return False





print(check())
