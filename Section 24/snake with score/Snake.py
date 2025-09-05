import turtle as t
from Food import Food
import math
import random as r
import scoreboard

class Snake():
    def __init__(self):
        self.snake_head = t.Turtle() # control the head and the make the body follow
        self.snake_head.shape('square')
        self.snake_head.color('white')
        self.snake_head.penup()
        self.snake_head.speed('slowest')

        self.food_obj = Food()

        self.snake_body = [] # add the turtles here every turtle here is the part of the    body
        self.sub_body_offset = 20  # default turtle size is 20 pixels
        self.direction = 'east'
        # PENDING DIRECTION LOGIC:
        # Instead of turning immediately when key is pressed, we queue the turn
        # and process it during move_fwd(). This ensures turn + move happen together
        # in the same frame, preventing rapid key presses from causing direction conflicts.
        # This is called "Input Buffering" - a common game programming pattern.
        self.pending_direction = None  # Queue for next direction change
        
        self.screen_obj = t.Screen()
        self.game_on = True
        self.start_size = 2
        self.body_size = self.start_size + 1

        self.scoreboard = scoreboard.Scoreboard()

    def init_snake(self):
        for i in range(1,self.start_size + 1):
            temp = t.Turtle()  # Create an instance, not just reference the class
            temp.shape('square')
            temp.color('white')
            temp.penup()  # Prevent drawing lines when moving
            temp.speed('slowest')
            temp.setx(-i * self.sub_body_offset)  # Use negative to offset behind head

            self.snake_body.append(temp)

        self.food_obj.spawn_food()

    def move_fwd(self):
        """
        Move the head forward and then for body, body_1 will get head coords, body_2 will get body_1 coords

        keep a list of previous positions
        """
        if self.game_on:
            if self.pending_direction:
                self.direction = self.pending_direction
                self.pending_direction = None
                
                # Set the heading based on direction
                if self.direction == 'north':
                    self.snake_head.setheading(90)
                elif self.direction == 'south':
                    self.snake_head.setheading(270)
                elif self.direction == 'west':
                    self.snake_head.setheading(180)
                elif self.direction == 'east':
                    self.snake_head.setheading(0)
            
            prev_pos = []
            # first get the previous postion of the head
            prev_pos.append((self.snake_head.xcor(),self.snake_head.ycor()))

            # then get the pevious position of the body ports
            for body in self.snake_body:
                body: t.Turtle
                prev_pos.append((body.xcor(),body.ycor()))

            # now update the positon of the head and the body
            self.snake_head.fd(20)
            for i,body in enumerate(self.snake_body):
                body: t.Turtle
                body.setpos(prev_pos[i])
        else:
            self.scoreboard.game_over_message()

    def turn_up(self):
        if self.direction != 'south':  # Can't turn up if going down
            self.pending_direction = 'north'

    def turn_down(self):
        if self.direction != 'north':  # Can't turn down if going up
            self.pending_direction = 'south'

            
    def turn_left(self):
        if self.direction != 'east':  # Can't turn left if going right
            self.pending_direction = 'west'

        
    def turn_right(self):
        if self.direction != 'west':  # Can't turn right if going left
            self.pending_direction = 'east'


    def check_bounds(self):
        if(self.snake_head.xcor() > self.screen_obj.window_width() // 2 - self.sub_body_offset or self.snake_head.ycor() > self.screen_obj.window_height() // 2 - self.sub_body_offset or self.snake_head.xcor() < -self.screen_obj.window_width() // 2 + self.sub_body_offset or self.snake_head.ycor() < -self.screen_obj.window_height() // 2 + self.sub_body_offset):
            self.snake_head.fd(0)
            self.game_on = False
    
    def check_collision_food(self):
        # print(f'food x: {self.food_obj.xcor()} food y: {self.food_obj.ycor()}')
        # print(f'snake x: {self.snake_head.xcor()} snake y: {self.snake_head.ycor()}')

        if math.sqrt((self.snake_head.xcor() - self.food_obj.xcor()) ** 2 + (self.snake_head.ycor() - self.food_obj.ycor()) ** 2) < 5.0:
            # if food is eaten then delete the food object and make a new one with random coords
            self.food_obj.ht()
            del self.food_obj
            self.food_obj = Food()

            # Add new segment at the last segment's position (or head if no body)
            extended_body = t.Turtle()
            extended_body.shape('square')
            extended_body.color('white')
            extended_body.penup()
            extended_body.speed('slowest')
            self.body_size += 1

            if self.snake_body:
                last_seg = self.snake_body[-1]
                extended_body.goto(last_seg.xcor(), last_seg.ycor())
            else:
                extended_body.goto(self.snake_head.xcor(), self.snake_head.ycor())
            self.snake_body.append(extended_body)

            self.scoreboard.incement_score()
    
    def check_self_collisoion(self):
        for body in self.snake_body[2:]:
            body: t.Turtle

            if math.sqrt((self.snake_head.xcor() - body.xcor()) ** 2 + (self.snake_head.ycor() - body.ycor()) ** 2) < 15.0:
                self.snake_head.fd(0)
                self.game_on = False
                break
    
    def game_status(self):
        return self.game_on
    def change_status(self):
        if self.game_on:
            self.game_on = False
        else:
            self.game_on = True
    
    def reset_snake(self):
        # self.game_on = True
        self.food_obj.hideturtle()
        del self.food_obj # remove the food object
        self.food_obj = Food()
        
        # clear the body
        for body in self.snake_body:
            body: t.Turtle
            body.hideturtle()
        self.snake_body.clear()
        self.snake_head.goto(0,0)
        self.direction = 'east'
        self.pending_direction = None
        self.body_size = self.start_size + 1
        self.init_snake() # reinitialize the snake
        self.scoreboard.write_score_after_reset()
        