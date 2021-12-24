from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='make your bet', prompt='which turtle will win the race? Enter a color: ')
colors = ['red','blue','yellow','green','purple', 'pink']
y_positions = [-70,-40,-10,20,50,70]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')    
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230,y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('your turtle won!!!')
                print(f'winning turtle {winning_color}')
            else:
                print('your turtle lost')
                print(f'winning turtle {winning_color}')

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
