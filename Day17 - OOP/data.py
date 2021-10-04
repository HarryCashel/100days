import json, urllib
import requests

URL = "https://opentdb.com/api.php?amount=25&category=9&difficulty=easy&type=boolean"

response = requests.get(URL)
data = response.json()

data = data['results']
