# def add(n1,n2):
#     return n1+n2

# def divide(n1,n2):
#     return n1/n2

# def multiply(n1,n2):
#     return n1*n2

# def subtract(n1,n2):
#     return n1-n2

# def calculated(calc_function, n1,n2):
#     return calc_function(n1,n2)

# user_input = input('-,+,/,* :')
# user_numbers = input('two numbers: ')
# num1 = int(user_numbers.split(' ')[0]) 
# num2 = int(user_numbers.split(' ')[1])

# if user_input == '-':
#     print(calculated(subtract,num1,num2))
# elif user_input == '+':
#     print(calculated(add,num1,num2))
# elif user_input == '/':
#     print(calculated(divide,num1,num2))
# else:
#     print(calculated(multiply,num1,num2))


#nested funcitons

# def outer_function():
#     print("I'm Outer")
#     def nested_function():
#         print("I'm inner")
#     return nested_function


# test = outer_function()
# test()


##Python decorator Funciton
import time

def decorator_function(function):
    def wrapper_funciton():
        before = time.time()
        function()
        after = time.time()
        print(f'{function.__name__}run speed:{after-before}')
    return wrapper_funciton


@decorator_function
def fast_function():
    for i in range(10000000):
        i * i

@decorator_function
def slow_function():
    for i in range(100000000):
        i * i        

fast_function()
slow_function()