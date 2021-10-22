from turtle import Turtle, Screen, back, forward, left, right
import random

colors = ['red','green','blue','gold','pink','purple','orange','lime','CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


tim = Turtle()
tim.shape('turtle')
tim.color('blue')
tim.pensize(10)
tim.speed(10)


dict_of_methods = [
    'forward',
    'right',
    'left',
    'backward'
]


shape = 0

while shape <=200:
    choice = random.choice(dict_of_methods)
    tim.pencolor(random.choice(colors))
    if choice == 'forward':
        tim.forward(30)
    elif choice == 'left':
        tim.left(90)
        tim.forward(30)
    elif choice == 'right':
        tim.right(90)
        tim.forward(30)
    else:
        tim.back(30)
    shape+=1






screen = Screen()
screen.exitonclick()

