# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
sheet_data = DataManager()

iata_codes = {city["iataCode"]: city["id"] for city in sheet_data.get_data()["prices"]}
# print(sheet_data.get_data()["prices"])
print(iata_codes)
flight_search = FlightSearch()
flight_search.destinations_list = iata_codes
flight_search.outbound_flights()
outbound_flights = flight_search.outbound_list
sheet_data.outbound_data = outbound_flights
print(outbound_flights)
# #
flight_search.inbound_flights()
inbound_flights = flight_search.inbound_list
sheet_data.inbound_data = inbound_flights
print(inbound_flights)
#

sheet_data.update_data("outboundPrice", outbound_flights, "outboundRoute", sheet_data.outbound_data)
sheet_data.update_data("inboundPrice", inbound_flights, "inboundRoute", sheet_data.inbound_data)
sheet_data.is_lower()
print(sheet_data.message)
