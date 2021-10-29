from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

s_board = ScoreBoard()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)


food = Food()
snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.end, 'e')



game_is_on = snake.end_game
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        s_board.increase_score()
    
    #detect collision with food
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake.reset()
            s_board.reset()

    if snake.end_game == False:
        game_is_on = snake.end_game
        snake.ending()
        

    #Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        snake.reset()
        s_board.reset()
        
        

        
        


    




screen.exitonclick()