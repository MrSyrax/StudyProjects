from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def move(self):
        self.forward(20)


    def reset_player(self):
        self.goto(0,-280)
        self.setheading(90)