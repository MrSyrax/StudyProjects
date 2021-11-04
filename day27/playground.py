# def add(*args):
#     x = 0
#     for nums in args:
#         x+=nums
#     return x

# total = add(1,2,3,4,5,6,7,8,9,10)
# print(total)

# def caculate(**kwargs):
#     n=0
#     print(kwargs)
#     # for key,value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n+= kwargs['add']
#     n*= kwargs['multiply']

# caculate(add=3,multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seats')



my_car = Car(make='Nissan', model='GT-R', colour='Black', seats='leather')

print(my_car.seats)