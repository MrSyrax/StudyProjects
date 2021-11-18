import json
user_input = input('type a word: ')

new_data = {
    user_input:{
        'name':'meep',
        '41': 31
    }
}

try:
    with open('Review/json/data.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    with open('Review/json/data.json', 'w') as file:
        json.dump(new_data,file, indent=4)
else:
    data.update(new_data)
    with open('Review/json/data.json', 'w') as file:
        json.dump(data, file, indent=4)
