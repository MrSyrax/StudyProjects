from turtle import Turtle
import random

COLORS = ['red','blue','orange','green']
'fastest','fast', 'normal','slow' 

class Car:
    def __init__(self):
        self.car_speed = 0.01
        self.cars_list = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            chosen_color = random.choice(COLORS)
            new_car.speed(self.car_speed)
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(chosen_color)
            new_car.penup()
            position1 = random.randint(-250,250)
            new_car.goto(300,position1)
            new_car.setheading(180)
            self.cars_list.append(new_car)


    def move_car(self):
        for car in self.cars_list:
            car.forward(10)