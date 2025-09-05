import turtle as t


turt = t.Turtle()
screen = t.Screen()
turt.speed('slowest')
screen.tracer(2,1)
dist = 2

for _ in range(200):
    turt.fd(dist)
    turt.rt(90)
    dist += 2


screen.exitonclick()