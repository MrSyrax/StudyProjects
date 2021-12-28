from tkinter.constants import N
from decouple import config
import requests
from datetime import datetime as dt


NUTRITION_API_K = config('NUTRITION_API_K')
APP_ID = config('APP_ID')

# -------------------------------Natural Language for exercise -------------------------------------------#
headers = {
'x-app-id':APP_ID,
'x-app-key':NUTRITION_API_K,
'Content-Type': 'application/json'
}

user_input = input('what Exercise(s) did you do today?: ')

body = {
 "query": user_input,
 "gender":"male",
 "weight_kg":99.7903,
 "height_cm":177.8,
 "age":32
    }

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
response = requests.post(url=exercise_endpoint,json=body,headers=headers)
new_dict = response.json()


#--------------------------------Manipulating Google Doc-------------------------------------------------#
now = dt.now()
time = now.strftime('%X %p')
date = now.strftime('%d/%m/%Y')

name = None
duration = None
calories = None

for value in new_dict['exercises']:
    name = value['name']
    duration = value['duration_min']
    calories = value['nf_calories']

    body = {
        'workout':{
            'date':date,
            'time': time,
            'exercise':name,
            'duration': duration,
            'calories': calories
        }
    }
    headers_for_sheety = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer chickensrarelylikeotherchickens'
    }

    add_row_endpoint = config('SHEET_ENDPOINT')

    response = requests.post(url=add_row_endpoint, json=body, headers=headers_for_sheety)

    print(response.text)
