import requests
import os
import pprint

GOOGLE_API = os.environ["GOOGLE_API"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = GOOGLE_API
        self._id = 2
        self.destination_data = None
        self.outbound_data = {}
        self.inbound_data = {}

    def get_data(self):
        response = requests.get(self.url)
        response.raise_for_status()

        # self.data = {city["iataCode"]: city["id"] for city in response.json()["prices"]}
        self.destination_data = response.json()["prices"]
        return response.json()

    def update_data(self, direction, direction_dict: dict, route):
        for dest in direction_dict:
            params = {
                "price": {
                    direction: direction_dict[dest]["price"],
                    route: self.format_dict(dest)

                }
            }
            response = requests.put(f"{GOOGLE_API}/{self._id}",
                                    json=params)
            response.raise_for_status()
            self._id += 1
        self._id = 2

    def format_dict(self, destination):
        route = self.outbound_data[destination]["route"]
        string = "\n".join([f"{key}: {value}" for key, value in route.items()])
        return string


# test = DataManager()
# print(test.get_data())
# print(test.destination_data)
#
# test.update_data("outboundPrice", test.outbound_data, "outboundRoute")
# test.update_data("inboundPrice", test.inbound_data, "inboundRoute")
