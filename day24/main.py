#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("day24/Input/Names/invited_names.txt") as names:
    names_to_invite = names.readlines()
    

with open('C:/Users/karey/Documents/Python/day24/Input/Letters/starting_letter.txt') as starting_letter:
    letter = starting_letter.read()

    for name in names_to_invite:
        stripped_name = name.strip()
        new_letter = letter.replace('[name]', stripped_name)
        with open(f'C:/Users/karey/Documents/Python/day24/Output/ReadyToSend/letter_to_{stripped_name}.txt','w') as completed_letter:
            completed_letter.write(new_letter)

     

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp