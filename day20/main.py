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

current_score = 0


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s_board.board(current_score)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        current_score+=1
        s_board.clear()
        


    
    
      










screen.exitonclick()