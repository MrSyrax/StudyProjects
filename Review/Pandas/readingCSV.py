# with open('MessAround/weather_data.csv') as file:
#     data = file.readlines()

# new_data = [n.strip() for n in data]

# print(new_data)

import pandas
from statistics import mean

# data = pandas.read_csv('Review/Pandas/weather_data.csv')

##can find columns wich start with the letter of your choosing, 
##can also use "contains" instead of startswith to find columns which contain your search 
# days_with_s = data.loc[data['day'].str.startswith('S')]

# print(days_with_s)

data = pandas.read_csv('Review/Pandas/weather_data.csv')
# temp_list = data['temp'].to_list()
# avg_temp = mean(temp_list)
# max_temp = max(temp_list)
# print(round(max_temp))

# max_temp = data[data['temp']==data['temp'].max()]
# print(max_temp)

# monday_row = data[data['day']=='Monday']

# monday_temp = monday_row['temp']*(9/5)+32

# # print(monday_temp)

# data_to_dict = data.to_dict()
# # print(data_to_dict)

# data_to_list = data['temp'].to_list()


# # data_to_str = data.loc[data['day'].str.contains('S')]

# avg_temp = round(data['temp'].mean())
# top_temp = data['temp'].max()

# highest_temp = data[data['temp'] == data['temp'].max()]
# print(highest_temp)

# data = pandas.read_csv('Review/Pandas/weather_data.csv')

# monday = data[data['day'] == 'Monday']

# print(f'Mondays Temp is: {int(monday.temp)*(9/5)+32}')


# data_dict = {
#     'animals':['tigers','lions','bears', 'wolves'],
#     'type': ['cool','supremo cool','supremo awesome','magnifico awesome'],
#     'scores':[1,2,3,4]
# }

# to_save = pandas.DataFrame(data_dict)

# to_save.to_csv('Review/Pandas/new_data.csv')

# print(str(monday.condition[0]))



data = pandas.read_csv('Review/Pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

red = 0
black = 0
grey = 0
no_color = 0

for colors in data['Primary Fur Color']:
    if colors == 'Cinnamon':
        red+=1
    elif colors == 'Black':
        black+=1
    elif colors == 'Gray':
        grey+=1
    else:
        no_color+=1


colors_dict = {
    'Fur Color':['grey','red','black','no color provided'],
    'Count':[grey,red,black,no_color]
}

colors_dict['Fur Color'].append('yes')

# print(colors_dict['Fur Color'])


new_data = pandas.DataFrame(colors_dict)
new_data.to_csv('Review/Pandas/new_data.csv')
