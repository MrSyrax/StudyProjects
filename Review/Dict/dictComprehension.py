# from random import randint

# names_list = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

# student_scores = {name:randint(0,100) for name in names_list}

# passed_students = {name:score for (name,score) in student_scores.items() if score > 60}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

result = {word:len(word) for word in sentence.split()}


# Write your code below:

print(result)




