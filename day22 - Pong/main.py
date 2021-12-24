from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Line
import time
import turtle

WINNING_AMOUNT = 4


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)



r_paddle = Paddle(( 350,0))
l_paddle = Paddle((-350,0))

r_score_board = Scoreboard((100,230))
l_score_board = Scoreboard((-140,230))

ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

line = Line()
line.write_line()
sleep_time = 0.06

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move_ball()
    line.write_line()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
        if sleep_time >= 0.01:
            sleep_time-=0.01
    
    if ball.xcor() > 400:
        l_score_board.clear()
        ball = Ball()
        ball.bounce_x()
        l_score_board.scored_point()
    elif ball.xcor() < -400:
        r_score_board.clear()
        ball = Ball()
        r_score_board.scored_point()

    if r_score_board.score == WINNING_AMOUNT:
        game_is_on = False
        
    elif l_score_board.score == WINNING_AMOUNT:
        game_is_on = False
        
    


screen.exitonclick()


