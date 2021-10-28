from turtle import  Screen, Turtle
from player import Player
from scoreboard import ScoreBoard
import cars as c
import time


cars_speed = ['slow','normal','fast','fastest']
counter = 0
#create screen and setup screen 
screen = Screen()
screen.setup(width=600,height=600)
#remove the start up animations
screen.tracer(0)
car = c.Car()

player = Player()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(player.move, 'Up')



game_is_on = True
while game_is_on:
    #create a small delay before updating the screen
    time.sleep(0.1)
    #show all after removing it with tracer(0)
    screen.update()
    
    car.create_car()
    car.move_car()
   
    #check if player made contact with any of the cars
    for cars in car.cars_list:

        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.player_lost()



    #check if the player has reached the top of the screen.
    if player.ycor() > 270:
        player.reset_player()
        car.car_speed *= .9
        scoreboard.update_score()



screen.exitonclick()
