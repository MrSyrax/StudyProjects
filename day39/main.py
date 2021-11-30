#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

sheet_info = DataManager()
flight_info = FlightSearch()
notifications=NotificationManager()

#pull in the sheet data and assign it to a variable named sheet_data
sheet_data = sheet_info.get_sheet_data()

#for each row in the sheet data (each dict in the json) grab the city name 
#to then pass on to get_iata_code and assign the row that is currently being seen iatacode
#with the one pulled from flight search
for row in sheet_data:
    if row['iataCode']=='':
        city_name =row['city']
        row['iataCode'] = flight_info.get_iata_code(city_name)

#update the sheet with the new data
sheet_info.update_sheet_data(sheet_data)

tomorow = datetime.now() + timedelta(days=1)
six_months_from_now = tomorow + timedelta(days=6*30)

for row in sheet_data:
    location_code = 'LON'
    destination_code = row['iataCode']

    price_check = flight_info.check_flights(location_code,destination_code,tomorow,six_months_from_now)
    try:
        if price_check.price < row['lowestPrice']:
            notifications.check_prices(
                price_check.price,
                price_check.origin_city,
                price_check.origin_aiport,
                price_check.destination_city,
                price_check.destination_aiport,
                price_check.out_date,
                price_check.return_date,
                price_check.stop_overs,
                price_check.stop_overs
            )
    except AttributeError:
        pass




