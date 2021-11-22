from typing import ByteString
import requests
import json
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from decouple import config



OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = config('api_key')
account_sid = config('account_sid')
auth_token = config('auth_token')
client = Client(account_sid,auth_token)
city = 'santa ana'
lat = 33.745472
lon = -117.867653
excluded_list = ['current,minutely,daily']

weather_params = {
    'lat': lat,
    'lon': lon,
    'exclude': excluded_list,
    'appid': api_key
}

data = requests.get(OWM_Endpoint, params= weather_params)
data.raise_for_status()
weather = data.json()

hourly_weather = weather['hourly'][:12]

list_of_ids = [n['weather'][0]['id'] for n in hourly_weather]

for id in list_of_ids:
    if int(id) < 700:
        x = True

try:
    if x:
        # proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

        # client = Client(account_sid, auth_token, http_client=proxy_client)
        message = client.messages \
                    .create(
                        body='Bring an Umbrella ☂️',
                        from_='+12565988358',
                        to='+17145925544'
                    )
        print(message.status)  
except NameError:
    pass




# try:
#     with open("C:/Users/Kareyo/Documents/Python/StudyProjects/day35/weather.json",'r') as file:
#         data = json.load(file)    
# except FileNotFoundError:
#     with open("C:/Users/Kareyo/Documents/Python/StudyProjects/day35/weather.json" , 'w') as file:
#         json.dump(weather["hourly"], file, indent=4)