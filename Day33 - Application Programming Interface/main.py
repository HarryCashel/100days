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





print(check())
