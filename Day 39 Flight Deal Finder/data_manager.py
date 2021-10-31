import requests
import os
import pprint

GOOGLE_API = os.environ["GOOGLE_API"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = GOOGLE_API
        self.destination_data = {city["iataCode"]: city["id"] for city in self.get_data()["prices"]}
        self.outbound_data = {}
        self.inbound_data = {}
        self.message = {}

    def get_data(self):
        response = requests.get(self.url)
        response.raise_for_status()

        # self.data = {city["iataCode"]: city["id"] for city in response.json()["prices"]}
        self.destination_data = response.json()["prices"]
        return response.json()

    def update_data(self, direction_price, direction_dict: dict, route):
        for dest in direction_dict:
            params = {
                "price": {
                    direction_price: direction_dict[dest]["price"],
                    route: self.format_dict(dest, direction_dict)

                }
            }
            response = requests.put(f"{GOOGLE_API}/{self.destination_data[dest]}",
                                    json=params)
            response.raise_for_status()

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
                total = float(city["outboundPrice"]) + float(city["inboundPrice"])
                if total < my_price:
                    self.message[city["city"]] = {
                        "city": city["city"],
                        "code": city["iataCode"],
                        "price": total,
                        "outbound": city["outboundRoute"],
                        "inbound": city["inboundRoute"]
                    }


# test = DataManager()
# print(test.get_data())
# print(test.destination_data)
# test.update_data()
# # test.is_lower()