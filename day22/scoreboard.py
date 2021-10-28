from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(f'{self.score}',font=('Arial', 40, 'bold'))

    def scored_point(self):
        self.score +=1
        self.write(f'{self.score}',font=('Arial', 40, 'bold'))
        
    
