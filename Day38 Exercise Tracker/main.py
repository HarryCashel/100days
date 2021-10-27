import requests
from datetime import datetime
import os

today = datetime.today().strftime('%Y%m%d')

KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
USER_ID = 0

# def test_endpoint():