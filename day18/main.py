import turtle as t
import random


t.colormode(255)
tim = t.Turtle()
tim.shape('turtle')
tim.pensize(10)
tim.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

colors = random_color()
directions = [0,90,180,270]

 

for _ in range(600):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))








screen = Screen()
screen.exitonclick()

