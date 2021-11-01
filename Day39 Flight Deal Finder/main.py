# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os

ACC_SID = os.environ["ACC_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]
FROM_NUM = os.environ["FROM_NUM"]
TO_NUM = os.environ["TO_NUM"]

sheet_data = DataManager()

flight_search = FlightSearch()
flight_search.destinations_list = sheet_data.destination_data
flight_search.outbound_flights()
outbound_flights = flight_search.outbound_list
sheet_data.outbound_data = outbound_flights
# print(outbound_flights)

flight_search.inbound_flights()
inbound_flights = flight_search.inbound_list
sheet_data.inbound_data = inbound_flights
# print(inbound_flights)


sheet_data.update_data("outboundPrice", outbound_flights, "outboundRoute", )
sheet_data.update_data("inboundPrice", inbound_flights, "inboundRoute",)
sheet_data.is_lower()
message_data = sheet_data.message
# print(message_data)
#
texter = NotificationManager(message_data, ACC_SID, AUTH_TOKEN, FROM_NUM, TO_NUM)
texter.send_message()
