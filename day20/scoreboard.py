from turtle import Turtle , Screen

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        
        self.penup()
        self.hideturtle()
        self.color('white')
        self.speed('fastest')
        self.goto(0,280)

    def board(self, score):
        self.write(f'Score: {score}', align='center', font=12)
