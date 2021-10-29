import os
from twilio.rest import Client


class NotificationManager:
    def __init__(self, message_list, sid, token, number, to_number):
        self.message_list = message_list
        self.sid = sid
        self.token = token
        self.number = number
        self.to_number = to_number

    def send_message(self):
        for flight in self.message_list:
            message = flight
            client = Client(self.sid, self.token)

            message = client.messages \
                .create(
                    body=message,
                    from_=self.number,
                    to=self.to_number
                )
        print(message.status)
