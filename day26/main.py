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



