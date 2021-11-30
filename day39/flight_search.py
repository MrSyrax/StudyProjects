import json
from typing import Type
from decouple import config
import requests
from requests.api import request
from pprint import pprint
from flight_data import FlightData

KIWI_KEY= config('KIWI_K')
KIWI_ENDPOINT= config('KIWI_ENDPOINT')


class FlightSearch:
    #this class is in charge of talking to the flight search api
    def __init__(self):
        self.sheet_data:json

    def get_iata_code(self, city_name):
        #create the headers for the query
        header={'apikey':KIWI_KEY}
        #create the query parameters
        query={'term': city_name, 'location"types':'city'}
        #capture the response from api
        response = requests.get(url=f'{KIWI_ENDPOINT}/locations/query',headers=header,params=query)
        #filter the response for the rows (dicts inside the jason)
        result = response.json()['locations']
        #filter the result further for the specific code 
        code = result[0]['code']
        #return the code
        return code

    def check_flights(self, origin_city_code , city_code, date_tomorrow, date_6months):
        header={'apikey':KIWI_KEY}
        query={
            'fly_from':origin_city_code,
            'fly_to': city_code,
            'date_from':date_tomorrow.strftime('%d/%m/%Y'),
            'date_to':date_6months.strftime('%d/%m/%Y'),
            'nights_in_dst_from':7,
            'nights_in_dst_to':28,
            'flight_type':'round',
            'one_for_city':1,
            'max_stopovers':0,
            'curr':'USD'
        }

        response = requests.get(url=f'{KIWI_ENDPOINT}/v2/search',headers=header,params=query)

        try:
            data = response.json()['data'][0]
        except IndexError:
            try:
                query['max_stopovers']=1  
                data = response = requests.get(url=f'{KIWI_ENDPOINT}/v2/search',headers=header,params=query)   
                data = response.json()['data'][0]

                flight_data = FlightData(
                price=data['price'],
                origin_city=data['cityFrom'],
                origin_aiport=data['route'][0]['flyFrom'],
                destination_city=data['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                out_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][1]['local_departure'].split('T')[0],
                stop_overs=1,
                via_city=data['route'][0]['cityTo']
                )
                return flight_data
            except IndexError:
                print('there are no flights for that ID')
        else:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data['cityFrom'],
                origin_aiport=data['route'][0]['flyFrom'],
                destination_city=data['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                out_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][1]['local_departure'].split('T')[0]
            )
            return flight_data
