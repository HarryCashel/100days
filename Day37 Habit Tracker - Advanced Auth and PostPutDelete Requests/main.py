import requests
from datetime import datetime

today = datetime.today().strftime('%Y%m%d')

pixel_url = "https://pixe.la/v1/users"
USERNAME = "cashmoney"
TOKEN = "qwertyuiop"


def create_user():
    params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(pixel_url, json=params)
    return response


def create_graph():
    graph_url = f"{pixel_url}/{USERNAME}/graphs"
    header = {"X-USER-TOKEN": TOKEN}
    paramas = {
        "id": "graph1",
        "name": "Study Time",
        "unit": "minutes",
        "type": "int",
        "color": "ajisai"

    }
    response = requests.post(graph_url, json=paramas, headers=header)
    response.raise_for_status()
    return response


# graph1 = create_graph()
# print(graph1.text)

def post_pixel(graph_id="graph1"):
    post_pixel_url = f"{pixel_url}/{USERNAME}/graphs/{graph_id}"
    header = {"X-USER-TOKEN": TOKEN}
    params = {
        "date": today,
        "quantity": "60",
    }
    response = requests.post(post_pixel_url, json=params, headers=header)
    response.raise_for_status()
    return response


def update_pixel(graph_id="graph1", date=today, quantity="60"):
    update_url = f"{pixel_url}/{USERNAME}/graphs/{graph_id}/{date}"
    header = {"X-USER-TOKEN": TOKEN}
    params = {
        "quantity": quantity,
    }
    response = requests.put(update_url, json=params, headers=header)
    response.raise_for_status()

    return response


def delete_pixel(graph_id="graph1", date=today):
    delete_url = f"{pixel_url}/{USERNAME}/graphs/{graph_id}/{today}"
    header = {"X-USER-TOKEN": TOKEN}

    response = requests.delete(delete_url, headers=header)
    response.raise_for_status()

    return response
