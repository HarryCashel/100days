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
        self.destinations_list = {}
        self.outbound_list = {}
        self.inbound_list = {}

    def api_call(self, dest, head, param, direction):
        response = requests.get(self.KIWI_URL, headers=head, params=param)
        response.raise_for_status()

        if response.json()["data"]:
            data = response.json()["data"][0]
            direction[dest] = {
                "price": data["price"],
                "fly_from": data["cityFrom"],
                "fly_to": data["cityTo"],
                "fly_from_code": data["cityCodeFrom"],
                "fly_to_code": data["cityCodeTo"],
                "route": {x["cityCodeTo"]: self.format_time(x["local_departure"]) for x in data['route']}
            }

    def outbound_flights(self):
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
            self.api_call(destination, header, flight_data, self.outbound_list)

    def inbound_flights(self):
        for destination in self.destinations_list:
            header = {"apikey": self.KIWI_API}
            flight_data = {
                "fly_from": destination,
                "fly_to": self._from,
                "date_from": today,
                "date_to": six_months,
                "one_for_city": 1,
                "curr": "AUD"
            }
            self.api_call(destination, header, flight_data, self.inbound_list)

    # noinspection PyMethodMayBeStatic
    def organise(self, data: dict):
        flight_data = data
        print(flight_data)

    # noinspection PyMethodMayBeStatic
    def format_time(self, iso_time):

        datetime_time = parser.isoparse(iso_time)
        format_time = datetime.strftime(datetime_time, "%d/%m/%Y %H:%M%p")
        return format_time
