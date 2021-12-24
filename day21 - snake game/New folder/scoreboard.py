from turtle import Turtle , Screen

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,260)
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def board(self):
        self.score+=1
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def lose(self):
        self.goto(-75, 0)
        self.color('white')
        self.write('Game Over!',font=('Arial', 24, 'normal'))
