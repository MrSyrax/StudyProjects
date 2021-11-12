# import smtplib

# # with open('C:/Users/karey/Documents/Python/day32/quotes.txt') as file:
# #     new_file = file.readlines()

# # print(new_file)

# my_email = 'kevinlearningpython@gmail.com'
# password = '5426233Kk!!'

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs='kevincarrillo89@yahoo.com', 
#         msg='Subject:Hello/n/nThis is the body of my email!')

import datetime as dt
import smtplib
from random import choice


my_email = 'kevinlearningpython@gmail.com'
password = '5426233Kk!!'

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()


if day_of_week == 4:
    with open('C:/Users/karey/Documents/Python/day32/quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote_of_the_day = choice(all_quotes)
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='jasminecarrillo1207@gmail.com', msg=f'Subject:Have a great Day!\n\n{quote_of_the_day}')



# date_of_birth = dt.datetime(year=1989 ,month=7 , day=12, hour=4)

# print(date_of_birth)