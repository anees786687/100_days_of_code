import turtle as t
from paddle import Paddle
import random
from ball import Ball
import math as m
class Opps(Paddle):
    PADDLE_Y = 0
    def __init__(self, screen: t.Screen, ball: Ball):
        super().__init__(screen, ball)
        self.screen = screen
        self.paddle_x = self.screen.window_width() // 2 - 2 * Paddle.PADDLE_WIDTH
        self.teleport(x= self.paddle_x, y = Opps.PADDLE_Y)
        self.direction = None

        self.score = 0
        self.opps_win = False

    def move_opps_paddle(self):
        """
        Idea is to move the paddle with ball and then check for collisions as well.

        to move the paddle with the ball, we get the difference between the ycords of the ball and paddle
        then we move the paddle with this difference
        """
        # first we move the paddle with the ball. Grab
        ball_y = self.ball.ycor()
        paddle_y = self.ycor()

        error = 0.2*(ball_y - paddle_y)
        new_y = self.ycor() + error

        screen_boundary = self.screen.window_height() // 2
        paddle_half_length = 50  # Half of paddle length
        
        if abs(error) > 5.0 and self.ball.xcor() >= 0 and int(self.ball.heading()) not in range(90,270):
            if new_y > screen_boundary - paddle_half_length:
                # Would go beyond top boundary
                new_y = screen_boundary - paddle_half_length
            elif new_y < -screen_boundary + paddle_half_length:
                # Would go beyond bottom boundary  
                new_y = -screen_boundary + paddle_half_length


            self.sety(new_y)

    def opp_score(self):
        if self.check_ball_collision() and self.ball.xcor() > self.xcor() - self.PADDLE_WIDTH // 2:
            self.score += 1

        if self.get_ball_collision_state() and self.ball.xcor() < 0:
            self.change_ball_collision_state()
    
    def set_opps_win(self):
        self.opps_win = True

    def get_opps_win(self):
        return self.opps_win
    
    def get_opps_score(self):
        return self.score
      