##################### Extra Hard Starting Project ######################
from datetime import datetime
import pandas
import random
import smtplib


my_email = 'kevinlearningpython@gmail.com'
password = '5426233Kk!!'

date = datetime.now()
date_to_check = (date.month,date.day)

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv('birthdays.csv')
birthdays = {index:data_row for (index, data_row) in data.iterrows()}

checker = 0
for n in range(len(birthdays)):
    dates = (birthdays[n]['month'], birthdays[n]['day'])
    if dates == date_to_check:
        name = birthdays[n]['name']
        email = birthdays[n]['email']
        checker+=1
    


if checker !=0:
    letters = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(letters) as letter:
        birthday_letter = letter.read()
        final_letter = birthday_letter.replace('[NAME]', name)
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=F'Subject:Happy Birthday!\n\n{final_letter}')