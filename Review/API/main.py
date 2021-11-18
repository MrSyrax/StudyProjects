#download and install requests module = pip install requests
import requests

#use the get method from requests to pull the data form the api
response = requests.get(url='https://api.kanye.rest/')

#format the data as a json file
data = response.json()

#print the data
print(data)

#pull speicifics out of the data
print(data['quote'])

