from email import message
from tkinter import *
import requests
from datetime import date, datetime
import smtplib

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

my_email = 'kevinlearningpython@gmail.com'
my_password = '5426233Kk!!'
MY_LAT = 33.745472
MY_LONG = -117.867653
long_lat = MY_LONG,MY_LAT
time_now = datetime.now()



response = requests.get('http://api.open-notify.org/iss-now.json')

data = response.json()

lng = float(data['iss_position']['longitude'])
lat = float(data['iss_position']['latitude'])

iss_position = (lng,lat)

parameters = {
    'lat':MY_LAT,
    'lng':MY_LONG,
    'formatted':0
}



response = requests.get(f'https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

if int(lat) in range(int(MY_LAT-10),int(MY_LAT+10)) and int(lng) in range(int(MY_LONG-10),int(MY_LONG+10)):
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(my_email,my_password)
            connection.sendmail(from_addr=my_email,to_addrs='kevincarrillo89@yahoo.com',msg='Subject:LOOK UP!\n\nLOOK UP THE ISS IS NEAR YOU')





