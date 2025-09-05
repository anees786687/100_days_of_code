from turtle import Turtle, Screen
from random import Random


r = Random()
turt = Turtle()
# make shape of the turtle 

# turt.shape("turtle")
# turt.color("red","green") # also accepts hex values for color#RRGGBB

### draw a square

# for _ in range(0,3):
#     turt.fd(200)
#     turt.rt(120)

### Dashed line
# Method 1
for _ in range(0,10):
    turt.fd(10)
    x, y = turt.position()
    turt.teleport(x + 10)

# Method 2
for _ in range(0,10):
    turt.fd(10)
    turt.pu()
    turt.fd(10)
    turt.pd()

### Drawing different shapes

for i in range(3, 11):
    angle = ((i - 2) * 180) / i
    tup = (r.random(),r.random(),r.random())
    turt.pencolor(tup)
    print(angle)
    for _ in range(0, i):
        turt.fd(100)
        turt.rt(180 - angle)

### random walk
turt.pensize(5)

direction = [0,90,180,270]
for _ in range(200):
    tup = (r.random(),r.random(),r.random())
    turt.pencolor(tup)
    turt.forward(30)
    turt.setheading(r.choice(direction))

turt.shape("arrow")

### spirograph
turt.speed('fastest')
for i in range(0,361):
    tup = (r.random(),r.random(),r.random())
    turt.pencolor(tup)
    turt.circle(80)
    turt.setheading(i)


screen = Screen()
screen.exitonclick()



