"""
1. Create a snake body
2. Move the snake
3. Create snake food
4. Detec collision with food
5. Increase snake body
6. Detect collision with wall
7. Detect collision with tail

"""

from turtle import Screen, Turtle
from random import Random 
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

# Initial setup
r = Random()
snake = Snake()
food_obj = Food()
score = Scoreboard()

# Screen setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake Game!")
screen.tracer(60)
screen.listen()
food = food_obj.show_food()
score_val = 0

# random points for food
food_point = r.randrange(-300,300)
snake.snake_init()
game_on = True
"""
in the game the snake appears to "wiggle" during its motion
this is becase the individual turtle object is moved 
so to prevent this and give a smooth animation we use
tracer() and update() methods of the Screen object

"""

while snake.snake_alive:
    screen.update()
    time.sleep(0.2)


    if snake.head.distance( food.pos()) < 15:
        print("yuum!")
        food.hideturtle()
        food.clear()
        
       
        food = food_obj.show_food()
        snake.generate_part()
        # print(f"{snake.snake_pos}")
        score.update_score()

    screen.onkey(key="Left",fun=snake.turn_left)
    screen.onkey(key="Right",fun=snake.turn_right)
    screen.onkey(key="Down",fun=snake.turn_down)
    screen.onkey(key="Up",fun=snake.turn_up)
    snake.move_snake()

score.game_over()
screen.exitonclick()
