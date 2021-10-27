from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self):
        self.segments = []

        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
        self.head = self.segments[0]
    
    def add_segment(self,position):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor,new_ycor)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DOWN:
            self.head.setheading(DOWN)
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            self.head.setheading(UP)
        else:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            self.head.setheading(RIGHT)
        else:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            self.head.setheading(LEFT)
        else:
            self.head.setheading(RIGHT)    