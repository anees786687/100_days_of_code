import turtle as t
import random as r

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.ht()
        self.penup()
        self.spawn_food()

    def spawn_food(self):
        self.ht()
        
        x = r.randrange(-220,220,20)
        y = r.randrange(-220,220,20)
        self.goto((x,y))
        self.st()