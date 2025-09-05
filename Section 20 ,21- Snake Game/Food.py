from turtle import Turtle, Screen
from random import Random
class Food():
    def __init__(self):
        self._r = Random()

        self._food_pos = None


    def _gen_point(self):
        self._food_pos = tuple([round(self._r.randint(-280,280)/20) * 20.0,round(self._r.randint(-280,280)/20) * 20.0])

    def show_food(self):
        self._gen_point()
        food = Turtle('circle')
        food.shapesize(0.5,0.5)
        food.color('red')
        food.penup()
        food.setpos(self._food_pos)
        food.showturtle()
        return food
    
    def get_position(self):
        return self._food_pos