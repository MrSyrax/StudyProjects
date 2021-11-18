from tkinter import *
import requests
from datetime import date, datetime


# def get_quote():
#     response = requests.get('https://api.kanye.rest/')
#     data = response.json()
#     canvas.itemconfig(text, text=data['quote'])


# window = Tk()
# window.title('Kanye Says')
# window.config(padx=50,pady=50)

# canvas = Canvas(width=300,height=414)
# back_ground = PhotoImage(file='day33/background.png')
# canvas.create_image(150, 207, image=back_ground)
# text = canvas.create_text(150, 207,text="Kanye Quote Goes HERE",width=250,font=('Arial',30,'bold'),fill='white')
# canvas.grid(column=0,row=0)

# kw_pic = PhotoImage(file='day33/kanye.png')
# button = Button(image=kw_pic,highlightthickness=0, command=get_quote)
# button.grid(column=0,row=1)


# window.mainloop()


MY_LAT = 33.745472
MY_LONG = -117.867653

time_now = datetime.now()
print(time_now.hour)


# response = requests.get('http://api.open-notify.org/iss-now.json')

# data = response.json()

# lng = data['iss_position']['longitude']
# lat = data['iss_position']['latitude']

#iss_position = (lng,lat)

parameters = {
    'lat':MY_LAT,
    'lng':MY_LONG,
    'formatted':0
}

response = requests.get(f'https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]


print(f'{sunrise} //// {sunset}')






