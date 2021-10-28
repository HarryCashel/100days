import os
import time

import requests
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from dateutil import parser

today = datetime.today().strftime('%d/%m/%Y')
six_months = (date.today() + relativedelta(months=+6)).strftime('%d/%m/%Y')


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.KIWI_API = os.environ["KIWI_API_KEY"]
        self.KIWI_URL = "https://tequila-api.kiwi.com/v2/search"
        self._from = "SYD"
        # may have to turn into dict - cityname: IATAcode
        self.destinations_list = ["PAR", "BER", "TYO"]
        self.price_list = {}

    def search_flights(self):
        for destination in self.destinations_list:
            header = {"apikey": self.KIWI_API}
            flight_data = {
                "fly_from": self._from,
                "fly_to": destination,
                "date_from": today,
                "date_to": six_months,
                "one_for_city": 1,
                "curr": "AUD"
            }
            response = requests.get(self.KIWI_URL, headers=header, params=flight_data)
            response.raise_for_status()
            data = response.json()["data"][0]
            self.price_list[destination] = {
                "price": data["price"],
                "fly_from": data["cityFrom"],
                "fly_to": data["cityTo"],
                "fly_from_code": data["cityCodeFrom"],
                "fly_to_code": data["cityCodeTo"],
                "route": {x["cityCodeTo"]: self.format_time(x["local_departure"]) for x in data['route']}
            }

            print(data)

    # noinspection PyMethodMayBeStatic
    def organise(self, data: dict):
        flight_data = data
        print(flight_data)

    # noinspection PyMethodMayBeStatic
    def format_time(self, iso_time):

        datetime_time = parser.isoparse(iso_time)
        format_time = datetime.strftime(datetime_time, "%d/%m/%Y %H:%M%p")
        return format_time


test = FlightSearch()
(test.search_flights())
print(test.price_list)

