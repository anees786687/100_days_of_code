# import colorgram
from turtle import Turtle, Screen
import random


# colors = colorgram.extract('hirst.jpg',30)
# color_list = []

# for i in colors:
#     color_list.append((i.rgb.r,i.rgb.g,i.rgb.b))

# print(color_list)

color_list = [(185, 162, 132), (129, 92, 70), (79, 93, 118), (147, 161, 180), (179, 152, 162), (210, 207, 135), (28, 35, 49), (119, 79, 92), (54, 24, 33), (46, 25, 19), (147, 170, 154), (86, 107, 91), (161, 156, 60), (113, 31, 43), (168, 107, 98), (27, 37, 33), (51, 58, 92), (212, 179, 189), (110, 123, 155), (117, 37, 27), (161, 107, 118), (219, 178, 170), (177, 202, 186), (180, 187, 209), (106, 144, 116), (67, 75, 35)]

tur = Turtle()
screen = Screen()
screen.screensize(900,900)
screen.colormode(255)
print(screen.screensize())
tur.pencolor("white")
tur.shapesize(2.0,2.0)
# tur.speed('fastest')
x = 725 - screen.window_width()
y = 500 - screen.window_height()
c_point = 0
tur.penup()
tur.hideturtle()
for _ in range(0,10):

    tur.setpos(x, y)
    for _ in range(0,10):
        tur.dot(20, random.choice(color_list))
        tur.fd(50)
    
    y += 50
    c_point += 1

screen.colormode(255)
screen.exitonclick()




