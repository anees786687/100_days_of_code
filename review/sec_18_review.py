# from turtle import Turtle, Screen

# tim = Turtle()

# tim.shape('turtle')
# tim.color('red','green')
# # draw a squre using turtle
# for _ in range(4):
#     tim.fd(100)
#     tim.rt(90)

# screen = Screen()
# screen.exitonclick()

import turtle as t
import random

# tim = t.Turtle()
# tim.speed('slowest')

# drawing dashed line
# tim.penup()
# for _ in range(10):
#     tim.pendown()
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)

""" Drawing multiple shapes 3,4,5,6,7 
    Interior Angle of a polygon is angle = [(n - 2) * 180] / n where n is the number of
    sides. Although the turtle turn angle is 180 - angle

    create an array which holds the number of sides.
    loop through this array, then define an inner loop which will draw the polygon
    move forward, then turn an angle calculated from the formula
 """

# draw different shapes
# sides = [3,4,5,6,7,8,9,10]
# for side in sides:
#     tim.pencolor((random.uniform(0.0, 255.0)/255, random.uniform(0.0, 255.0)/255, random.uniform(0.0, 255.0)/255))
#     angle = 360 / side # get the interior angle of the polygon
#     for _ in range(side):
#         tim.fd(100)
#         tim.rt(angle)

"""random walk"""
# tim.pen(pensize=5)
# tim.speed('fastest')
# angles = [0,90,180,270]



# screen = t.Screen()

# # Define boundaries (leaving some margin from edges)
# boundary_x = screen.window_width() // 2 - 50
# boundary_y = screen.window_height() // 2 - 50

# for _ in range(200):
#     # Check all four boundaries
#     if(tim.xcor() > boundary_x):
#         tim.setheading(180)
#     elif(tim.xcor() < -boundary_x):
#         tim.setheading(0)
#     elif(tim.ycor() > boundary_y):
#         tim.setheading(270)
#     elif(tim.ycor() < -boundary_y):
#         tim.setheading(90)
#     else:
#         tim.rt(random.choice(angles))
#     tim.pencolor((random.uniform(0.0, 255.0)/255, random.uniform(0.0, 255.0)/255, random.uniform(0.0, 255.0)/255))
#     tim.fd(50)


"""Making Spirograph"""
# tim = t.Turtle()
# tim.speed('fastest')
# screen = t.Screen()
# current_heading = 0
# tim.setheading(current_heading)
# for _ in range(360 // 5):
#     current_heading += 5
#     tim.setheading(current_heading)
#     tim.pencolor((random.uniform(0.0, 255.0)/255, random.uniform(0.0, 255.0)/255, random.uniform(0.0, 255.0)/255))

#     tim.circle(100)

# screen.exitonclick()


"""Hirst Painting"""
tim = t.Turtle()
screen = t.Screen()

start_x = -300.0
start_y = -300.0
tim.teleport(start_x, start_y, fill_gap=False)

for i in range(20):
    for j in range(20):
        tim.pencolor((random.uniform(0.0, 255.0)/255, random.uniform(0.0, 255.0)/255, random.uniform(0.0, 255.0)/255))
        tim.dot(size=10)
        tim.penup()
        tim.fd(30)
        tim.pendown()
    start_y+=30
    tim.teleport(start_x, start_y)
screen.exitonclick()
