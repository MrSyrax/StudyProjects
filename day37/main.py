import json
import requests
from decouple import config
from datetime import datetime as dt
from tkinter import *



# window = Tk()

# year_entry = Entry(width=10)
# year_entry.grid(column=0,row=0)

# month_entry = Entry(width=10)
# month_entry.grid(column=0,row=1)

# day_entry = Entry(width=10)
# day_entry.grid(column=0,row=2)

# user_selected_date = 0

# def update_date():
#     global user_selected_date
#     selected_year = year_entry.get()
#     selected_month = month_entry.get()
#     selected_day = day_entry.get()
#     user_selected_date = dt(year=int(selected_year), month=int(selected_month), day=int(selected_day))

# button = Button(text='poooosh me', command=update_date)
# button.grid(column=0, row=3)


# window.mainloop()

# print(user_selected_date)

current_date = dt.now()

formated_date = current_date.strftime("%Y%m%d")

TOKEN = config('TOKEN')
USERNAME = config('USERNAME1')
GRAPH = 'graph1'


pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# resposne = requests.post(url=pixela_endpoint, json=user_params)
# print(resposne.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Study Graph',
    'unit' : 'Hr',
    'type': 'float',
    'color': 'kuro'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# resposne = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(resposne.text)


#post
pixel_creation_endpoint = f'{graph_endpoint}/{GRAPH}'

update_params = {
    'date': formated_date,
    'quantity':'6'
}

# resposne = requests.post(url=pixel_creation_endpoint, json=update_params, headers=headers)
# print(resposne.text)

#Put
pixel_update_endpoint = f'{pixel_creation_endpoint}/20211122'

update_pixel_params = {
    'quantity':'5'
}


# resposne = requests.put(url=pixel_update_endpoint,json=update_pixel_params,headers=headers)
# print(resposne.text)

#Delete 
response = requests.delete(url = pixel_update_endpoint, headers=headers)
print(response.text)