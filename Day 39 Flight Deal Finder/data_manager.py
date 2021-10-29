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
        self.message = {}

    def get_data(self):
        response = requests.get(self.url)
        response.raise_for_status()

        # self.data = {city["iataCode"]: city["id"] for city in response.json()["prices"]}
        self.destination_data = response.json()["prices"]
        return response.json()

    def update_data(self, direction_price, direction_dict: dict, route, direction):
        for dest in direction_dict:
            params = {
                "price": {
                    direction_price: direction_dict[dest]["price"],
                    route: self.format_dict(dest, direction)

                }
            }
            response = requests.put(f"{GOOGLE_API}/{self._id}",
                                    json=params)
            response.raise_for_status()
            self._id += 1
        self._id = 2

    def format_dict(self, destination, direction):
        route = direction[destination]["route"]
        string = "\n".join([f"{key}: {value}" for key, value in route.items()])
        return string

    def is_lower(self):
        for city in self.get_data()["prices"]:
            # print(city)
            if city["inboundPrice"] and city["outboundPrice"]:
                # print("yes")
                my_price = city["myLowestPrice"]
                total = city["outboundPrice"] + city["inboundPrice"]
                if total < my_price:
                    self.message[city["city"]] = {
                        "city": city["city"],
                        "code": city["iataCode"],
                        "price": total,
                        "outbound": city["outboundRoute"],
                        "inbound": city["inboundRoute"]
                    }

# test = DataManager()
# test.is_lower()
