# import turtle

#  the above can be written as

from turtle import Turtle, Screen

# we will use the Turtle class in the turtle module
t_obj = Turtle()
my_screen = Screen() # making a screen object

# setting up a turtle
t_obj.shape("turtle")
t_obj.color("red","green") # setting color of the turtle object (BorderColor, FillColor)
t_obj.fd(100) # moving the turtle forward by 100pixes


# Setting canvas height and width, defautl is 300 x 300 
my_screen.exitonclick() # mthod that exits the screen once the click is detected on the screen

