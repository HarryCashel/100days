import requests

URL = "https://opentdb.com/api.php?"

parameters = {
    "amount": "10",
    "type": "boolean"
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()["results"]

answer = data[0]["question"]
print(answer)