import pandas

list_1 = [100,200,300]
list_2 = ['a','b','c']
list_3 = ['orange','santa ana','LA']

#create a dictionary 
new_dict_comp = {list_1[n]:list_2[n] for n in range(len(list_1))}
# print(new_dict_comp)
print(new_dict_comp)

#create an enumerated dictionary of tuples 
new_dict = dict(enumerate(zip(list_1,list_2)))
print(new_dict)

#print out tuples from two lists
for n in zip(list_1,list_2):
    print(n)

#create a list of dictionaries from 2 lists
to_write = [{list_1[n]:list_2[n]} for n in range(len(list_1))]

#create a list of dictionaries from 3 lists (can be made into a pandas DataFrame)
to_write = [{
    'price': list_1[n],
    'link': list_2[n],
    'address': list_3[n]
} for n in range(len(list_1))]

#use pandas to create a data fram from the above dictionary
writable = pandas.DataFrame(to_write)
#use the newly created data frame to create a new csv called test
writable.to_csv('test.csv', index=False)
#use pandas to read test.csv and save the contests to the variable "to_read"
to_read = pandas.read_csv('test.csv')
#print the above csv
print(to_read)