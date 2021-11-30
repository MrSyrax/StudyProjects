from typing import Text
from twilio.rest import Client
from decouple import config


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):

        self.twilio_key=config('TWILIO_K')
        self.twilio_sid=config('TWILIO_SID')
        self.client = Client(self.twilio_sid,self.twilio_key)
        

    def check_prices(self, low_price, from_loc, from_code, to_loc, to_code, out_date, in_date,stop_overs):
        #I need to get the current price per item from the sheet
        text = f'Low price alert! Only ${low_price} to fly from {from_loc}-{from_code} to {to_loc}-{to_code}, from{out_date} to {in_date}'
        if stop_overs > 0:
            text = f'Low price alert! Only ${low_price} to fly from {from_loc}-{from_code} to {to_loc}-{to_code}, from{out_date} to {in_date}'
        message = self.client.messages.create(
            body=text,
            from_=+12565988358,
            to=+17145925544
        )
        print(message.status)