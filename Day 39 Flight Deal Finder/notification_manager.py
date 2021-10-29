import os
from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.message_list = []
        self.sid = None
        self.token = None
        self.number = None
        self.to_number = None

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
