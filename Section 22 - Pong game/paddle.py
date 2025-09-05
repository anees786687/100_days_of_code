from turtle import Turtle, Screen
class Paddle(Turtle):
    def __init__(self, x_value: int, screen: Screen):
        super().__init__("square", visible=True)
        self.screen = screen
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.setx(x_value)
        self.left(90)
        self._r_direction = None # initial direction of paddle
        
    def move_up(self):
        if self.ycor() + 50 >= self.screen.window_height() // 2:  
            return
        self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() - 50 <= -self.screen.window_height() // 2:  
            return
        self.sety(self.ycor() - 20)

    # moving the right paddle
    def move_right_paddle(self, ball):

        """
        This function will move the right paddle up and down based on the 
        position of the ball

        idea is to get the current position of the ball, the ball x and y coords are changing
        so we have to change y coords of right paddle so that when
        """
        self._paddle_controller(ball)
    
    def _check_limits(self, direction):
        if direction == "up" and self.ycor() + 50 >= self.screen.window_height() // 2:
            return True
        if direction == "down" and self.ycor() - 50 <= -self.screen.window_height() // 2:
            return True
        return False
    
    def _paddle_controller(self, ball):
        from ball import Ball 

        """
        Implements a P controller to move the right paddle automatically
        based on the ball's Y position.
        """
        Kp = 0.5  # Tuning parameter (reduce if paddle moves too fast) use this to set difficulty
        threshold = 5  # Acceptable error before stopping correction

        # Get the ball's current Y position (process variable)
        current_ball_y = ball.ycor()
        

        # Get the paddle's target position (setpoint)
        final_paddle_y = self.ycor()

        # Compute error (difference between setpoint and process variable)
        pos_error = current_ball_y - final_paddle_y

        # Calculate correction (Proportional control)
        change = Kp * pos_error  # Adjust movement

        new_y = self.ycor() + change

        # prevent moving beyond the screen
        if abs(pos_error) > threshold:  # Move only if error is significant
            if new_y + 50 > self.screen.window_height() // 2:  # Top limit
                new_y = self.screen.window_height() // 2 - 50
            elif new_y - 50 < -self.screen.window_height() // 2:  # Bottom limit
                new_y = -self.screen.window_height() // 2 + 50

        # Apply the movement
            self.sety(new_y)
