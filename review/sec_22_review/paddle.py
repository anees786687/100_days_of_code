import turtle as t
import math as m
from ball import Ball
class Paddle(t.Turtle):
    PADDLE_WIDTH = 20
    PADDLE_LENGTH = 100

    def __init__(self, screen: t.Screen, ball: Ball):
        super().__init__()
        self.screen = screen
        self.shape('square')
        self.color('white', 'white')
        self.shapesize(stretch_wid=1.0,stretch_len=5.0)
        self.penup()
        self.setheading(90)

        self.ball = ball
        self.ball_collided = False
        self.paddle_hit = False

    def check_boundary_collision(self):
        """
        This checks the collision of the paddle with the upper and lower boundary
        if the center of the paddle is 50 pixels away from the upper or lower boundary
        then cease the movement of the paddle
        """
       
        screen_boundary = self.screen.window_height() // 2
        if abs(self.ycor()) >= screen_boundary - Paddle.PADDLE_LENGTH // 2:
            return True
        
        return False
    
    def check_ball_collision(self):
        ball_x = self.ball.xcor()
        ball_y = self.ball.ycor()
        dist = self.distance(ball_x,ball_y)

        if not self.ball_collided:
            if dist < 50 and abs(self.xcor() - ball_x) < Paddle.PADDLE_WIDTH // 2:
                self.ball.setheading(180 - self.ball.heading())
                self.ball_collided  = True
                return True
        
        return False
    
    def change_ball_collision_state(self):
        self.ball_collided = False
    
    def get_ball_collision_state(self):
        return self.ball_collided
        
    
