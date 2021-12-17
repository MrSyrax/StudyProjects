import os
import time

class User:
    def __init__(self, name,id):
        self.name = name
        self.id = id
        self.is_logged_in = False
        self.blog_post_amount = 0

user_1 = User('Kevin', '02341920')

def auth_check(function):
    def wf(*args, **kwargs):
        if args[0].is_logged_in == True:
           return function(args[0])
        else:
            print('You must log in before being able to post')
    return wf

@auth_check
def new_blog_post(user):
    if user.blog_post_amount < 1:
        return f"This is {user.name}'s first blog post!"
    else:
        return f"This is {user.name}'s New Blog Post"


user_1.is_logged_in = True

response = new_blog_post(user_1)
time.sleep(2)
os.system(f"echo {response} >> test.txt")