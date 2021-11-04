import colorgram

color_list = [(249, 243, 247), (1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), 
(149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), 
(11, 96, 57), (95, 6, 20), (174, 135, 163), 
(1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), 
(8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178)]


tim = t.Turtle()
tim.speed(10)
t.colormode(255)
tim.penup()
y = 0 

for _ in range(10):
    for _ in range(10):
        color_chosen = random.choice(color_list)
        tim.color(color_chosen)
        tim.dot(20)
        tim.forward(50)

    y +=40
    tim.sety(y)
    tim.setx(0)    

screen = t.Screen()
screen.exitonclick()

