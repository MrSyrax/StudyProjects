from art import logo, vs
import random
from game_data import data
from os import system

#print the logo
print(logo)

#create two empty dictionaries chose a random dictionary from game_data.data

f_dict = random.choice(data)
s_dict = random.choice(data)
if f_dict == s_dict:
    s_dict = random.choice(data)
    


print(f"{f_dict['name']}, {f_dict['description']}, {f_dict['country']}")
print(vs)
print(f"{s_dict['name']}, {s_dict['description']}, {s_dict['country']}")
#ask the user to guess who has more followers
user_choice = input('\nwho do you think has more Instagram followers?\nType their name below:\n')
#evaluate the user_choice 
winning = False
winning_choice = {}
user_value = 0

if user_choice.lower() == f_dict['name'].lower():
    user_value = f_dict['follower_count']
    if user_value > s_dict['follower_count']:
        print('Good Job')
        winning_choice = f_dict
        winning = True

        while winning:
            system('clear')
            print('Good Job')

            print(logo)

            f_dict = random.choice(data)

            print(f"{winning_choice['name']}, {winning_choice['description']}, {winning_choice['country']}")
            
            print(vs)
            
            print(f"{f_dict['name']}, {f_dict['description']}, {f_dict['country']}")

            user_choice = input('\nwho do you think has more Instagram followers?\nType their name below:\n')

            if user_choice.lower() == f_dict['name'].lower():
                user_value = f_dict['follower_count']
                if user_value > winning_choice['follower_count']:
                    system('clear')
                    print('Good Job')
                    winning_choice = f_dict
                else:
                    system('clear')
                    print('you lose')
                    winning = False
            else:
                user_value = winning_choice['follower_count']
                if user_value > f_dict['follower_count']:
                    system('clear')
                    print('You win')
                else:
                    system('clear')
                    print('you lose')
                    winning = False
            
    else:
        system('clear')
        print('you lose')
else:
    user_value = s_dict['follower_count']
    if user_value > f_dict['follower_count']:
        print('You win')
        winning_choice = s_dict
        winning = True

        while winning:
            system('clear')
            s_dict = random.choice(data)
            print(logo)

            print(f"{winning_choice['name']}, {winning_choice['description']}, {winning_choice['country']}")
        
            print(vs)

            print(f"{s_dict['name']}, {s_dict['description']}, {s_dict['country']}")

            user_choice = input('\nwho do you think has more Instagram followers?\nType their name below:\n')

            if user_choice.lower() == s_dict['name'].lower():
                user_value = s_dict['follower_count']
                if user_value > winning_choice['follower_count']:
                    print('Good Job')
                    winning_choice = s_dict
                else:
                    system('clear')
                    print('you lose')
                    winning = False
            else:
                user_value = winning_choice['follower_count']
                if user_value > s_dict['follower_count']:
                    print('You win')
                else:
                    system('clear')
                    print('you lose')
                    winning = False
                      
    else:
        system('clear')
        print('you lose')
      