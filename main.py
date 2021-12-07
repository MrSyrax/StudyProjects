# word = "Indivisibilities"
# user_in_to_list = list(word)

# dupes = dict()

# for character in user_in_to_list:
#     if character in dupes:
#         dupes[character] += 1
#     else:
#         dupes[character] = 1

# for key, value in dupes.items():
#     print(f"{key} appeared {value} times")

# def find_duplicate():
#     x =input("Enter a word = ").lower()
#     for char in x :
#         counts=x.count(char)
#         print(char,counts)

# find_duplicate()

def find_duplicate(x):
    result = {}
    for char in set(x):
        result[char]=x.count(char)
        for key,value in result.items():
            if value >1:
                print(value)

find_duplicate('Indivisibilities'.lower())