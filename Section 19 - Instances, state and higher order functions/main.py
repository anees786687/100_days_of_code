from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

def move_forward():
    tim.fd(10)

def turn_left():
    tim.lt(90)

    
def move_backward():
    tim.bk(10)

def turn_right():
    tim.rt(15)

def reset():
    tim.reset()
screen.listen() # tells the screen object to start listening

# we have to bind a function for the screen to listen, these are event listeners
# on example is onkey()
# we have to bind a function to this listener
# PASSING ARGS USING KEYWORD ARGS
screen.onkey(key="Up", fun=move_forward) # binds move forward 
screen.onkey(key="Down", fun=move_backward) # binds move backward
screen.onkey(key="Left", fun=turn_left) # binds turn left
screen.onkey(key="Right", fun=turn_right) # binds turn right
# PASSING ARGS AS POSITIONAL ARGS
screen.onkey(reset, "c")
screen.exitonclick()

