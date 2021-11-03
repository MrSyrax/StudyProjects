import csv
import pandas
import statistics as s

from pandas.core.series import Series


# path to data on home pc C:\Users\Kareyo\Documents\Python\StudyProjects\day25\weather_data.csv
#path to data on gaming pc 'C:/Users/karey/Documents/Python/day25/weather_data.csv'
data = pandas.read_csv('C:/Users\Kareyo\Documents\Python\StudyProjects\day25\weather_data.csv')   

avg = round(data['temp'].mean())
max_temp = data['temp'].max()

print(f'average temp for the week is: {avg}\nThe Max temp for the week was: {max_temp}')