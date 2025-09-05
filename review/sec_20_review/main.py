import turtle as t
import random as r
import time  # Add this import for sleep
from Snake import Snake  # Import the Snake class from Snake.py


screen = t.Screen()
screen.setup(width=500, height=500)
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
snake.init_snake()

# Set up key bindings ONCE, outside the loop
screen.onkeypress(snake.turn_up,"w")
screen.onkeypress(snake.turn_down,'s')
screen.onkeypress(snake.turn_left,'a')
screen.onkeypress(snake.turn_right,'d')
screen.listen()  # Enable listening for key events

while True:
    snake.move_fwd()
    screen.update()

    snake.check_bounds()
    snake.check_collision_food()
    snake.check_self_collisoion()

    time.sleep(0.15)  # Reduced delay for more responsive controls

screen.exitonclick()