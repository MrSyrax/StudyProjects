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

phonetic_alphabet = pandas.read_csv('C:/Users/karey/Documents/Python/day26/nato_phonetic_alphabet.csv')
pa_dict = {code.letter:code.code for (index, code) in phonetic_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code codes from a word that the user inputs.

def generate_phonetic():
    user_input = input('Enter a code: ')
  
    if user_input != 'Exit':
        try:
            phonetic_list = [pa_dict[n.upper()] for n in user_input]
        except KeyError:
            print('pleae only letters in the english alphabet')
            generate_phonetic()
        else:
            print(phonetic_list)

generate_phonetic()
    