import pandas

list_1 = [100,200,300]
list_2 = ['a','b','c']
list_3 = ['orange','santa ana','LA']

# new_dict_comp = {list_1[n]:list_2[n] for n in range(len(list_1))}

# print(new_dict_comp)
# # print(new_dict_comp)

# new_dict = dict(enumerate(zip(list_1,list_2)))
# print(new_dict)

# for n in zip(list_1,list_2):
#     print(n)


# to_write = [{list_1[n]:list_2[n]} for n in range(len(list_1))]

to_write = [{
    'price': list_1[n],
    'link': list_2[n],
    'address': list_3[n]
} for n in range(len(list_1))]

writable = pandas.DataFrame(to_write)
writable.to_csv('test.csv', index=False)

to_read = pandas.read_csv('test.csv')

print(to_read)