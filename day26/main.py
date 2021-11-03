<<<<<<< HEAD
# numbers = [1,2,3]
# new_numbers = [n + 1 for n in numbers]

# print(new_numbers)

# name = 'Angela'
# new_list = [letter for letter in name]
# print(new_list)


# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [n.upper() for n in names if len(n)>4]

# print(short_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# result = [n for n in numbers if n%2==0]

# print(result)



# new_dict = {new_key:new_value for item in list}

# new_dict = {new_key:new_value for (key,value) in dict.items() }

# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

import random

score_list = {student:random.randint(1,100) for student in names}

print(score_list)

passed_student = {student: score for (student, score) in score_list.items() if score >= 60}

print(passed_student)



=======
# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     student = key
#     score = value

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keycode Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

import pandas

phonetic_alphabet = pandas.read_csv('C:/Users/Kareyo/Documents/Python/StudyProjects/day26/nato_phonetic_alphabet.csv')
pa_dict = {code.letter:code.code for (index, code) in phonetic_alphabet.iterrows()}


#TODO 2. Create a list of the phonetic code codes from a word that the user inputs.

guessing_names = True
while guessing_names:

    user_input = input('Enter a code: ')
    if user_input != 'Exit':

        phonetic_list = [pa_dict[n.upper()] for n in user_input]
        print(phonetic_list)
    else:
        break
>>>>>>> d2e75dd80f7aacae961c5549b3c76e5b53d9c47e
