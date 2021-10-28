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
        
    
    def player_won(self):
        self.color('white')


class Line(Turtle):
    def __init__(self):
        super().__init__()
        
        self.step = 0
        self.pensize(10)
        self.color('white')
        self.penup()
        self.goto(0,300)
        self.setheading(270)

    def write_line(self):
        for _ in range(0,100):
            self.forward(40)
            self.pendown()
            self.forward(40)
            self.penup()
            

            


        
        
        