from turtle import Turtle, Screen
screen = Screen()
t = Turtle()
screen.tracer(8, 25)

dist = 2

for i in range(200):

    t.fd(dist)

    t.rt(90)

    dist += 2

screen.mainloop()