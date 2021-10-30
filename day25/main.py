import csv
import pandas

# with open('C:/Users/karey/Documents/Python/day25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))



data = pandas.read_csv('C:/Users/karey/Documents/Python/day25/weather_data.csv')            
print(data)