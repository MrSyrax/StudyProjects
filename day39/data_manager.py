import json
import requests
from pprint import pp, pprint
from decouple import config

URL=config('SHEETY_ENDPOINT')

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_data:requests
        self.data:json
      
    
    def get_sheet_data(self):
        #gets all the sheet data
        self.get_data=requests.get(url=URL)
        #gets the rows list (rows) in the json
        self.data=self.get_data.json()['prices']
        return self.data


    def update_sheet_data(self, sheetdata):
        #for each dict in the json passed in check the 'id' and the 'iatacode' and then update the sheet row by row
        for row in sheetdata:
            id = row['id']
            iatacode=row['iataCode']
            new_data={
                'price':{
                    'iataCode':iatacode
                }
            }
            requests.put(url=f'{URL}/{id}',json=new_data)

