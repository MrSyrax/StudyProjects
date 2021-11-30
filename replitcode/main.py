import requests
from decouple import config
from pprint import pprint

sheety_user_endpoint=config('SHEETY_USER_ENDPOINT')

response = requests.get(url=sheety_user_endpoint)
user_info = response.json()

print (user_info)



print("Welcome to Kevin' Flight Club.\nWe find the best flight deals and email you.")
first_name=input("What is your first name?\n")
last_name=input("what is your last name?\n")

same_email = True
while same_email:
    email=input('what is your email?\n')
    email2=input('please re-enter your email\n')
  
    if email == email2:
        body={
            'user':{
                'firstName':first_name,
                'lastName': last_name,
                'email': email
                }
        }
        
        response = requests.post(url=sheety_user_endpoint,json=body)
        print('welcome to the club!')
        same_email=False
    else:
        print("oops looks like you didn't enter the same email\nplease retry")