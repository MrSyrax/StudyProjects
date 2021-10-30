import csv
import pandas
import statistics as s

from pandas.core.series import Series


# path to data on home pc C:\Users\Kareyo\Documents\Python\StudyProjects\day25\weather_data.csv
#path to data on gaming pc 'C:/Users/karey/Documents/Python/day25/weather_data.csv'
data = pandas.read_csv('C:/Users\Kareyo\Documents\Python\StudyProjects\day25\weather_data.csv')   
# data_dict = data.to_dict()         
# # print(data_dict)
# temp_list = data['temp'].to_list()


# total_temp = round(data['temp'].mean())
# max_temp = data['temp'].max()

# print(total_temp)
# print(max_temp)
# print(type(data))
# print(data)
print(data[data['day'] == 'Monday'])