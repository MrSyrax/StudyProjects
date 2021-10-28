from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.current_score = 0
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.write(f'Level: {self.current_score}', font=('Arial',20,'bold'))


    def update_score(self):
        self.clear()
        self.current_score+=1
        self.write(f'Level: {self.current_score}', font=('Arial',20,'bold'))

    def player_lost(self):
        self.goto(-60,0)
        self.write('Game Over!',font=('Arial',20,'bold'))

    def player_won(self):
        self.goto(-60,0)
        self.write('You Won!',font=('Arial',20,'bold'))