from turtle import Turtle, Screen
import random as r
from paddle import Paddle

class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.screen = Screen()
        self.color('white')
        self.penup()
        self.angles = r.choice(((45,60),(-60,-45),(120,135),(-135,-120)))
        self.angle = r.randint(self.angles[0],self.angles[1])
        self.setheading(self.angle)
        self.ball_direction = "up" if self.angle > 0 else "down"
        self.current_y = self.ycor()
        self.prev_y = self.current_y 
        self.last_paddle_hit = None  # Store last hit paddle

    def move_ball(self):

        """
            Moves the ball forward in its current direction and handles collisions 
            with the top and bottom walls.

            Movement:
            - The ball moves forward by a fixed distance (e.g., 10 units).
            - The movement direction is determined by the ball’s heading (angle).

            Collision Handling:
            - If the ball hits the **top boundary** (`y > screen.window_height() // 2`), 
            it reflects downward by negating its heading.
            - If the ball hits the **bottom boundary** (`y < -screen.window_height() // 2`), 
            it reflects upward by negating its heading.

            Recursion:
            - The function calls itself using `screen.ontimer(move_ball, 50)`, 
            ensuring continuous movement every 50 milliseconds.

            Notes:
            - This function must be called once to start the ball movement.
            - It relies on `screen.window_height()` for accurate boundary detection.
        """
        self.forward(10)  # Adjust speed

        # Corrected collision detection using window size
        if self.ycor() > self.screen.window_height() // 2 - 20:
            self.setheading(-self.heading())  # Reflect down
            self.ball_direction = "down"
        elif self.ycor() < -self.screen.window_height() // 2 + 20:
            self.setheading(-self.heading())  # Reflect up
            self.ball_direction = "up"
       
    def check_collision(self, paddle: Paddle):
        """
        Prevent multiple hits by checking if the ball has left the paddle before allowing a new hit.
        """
        if self.distance(paddle) < 50 and abs(self.xcor() - paddle.xcor()) < 29:
            if self.last_paddle_hit == paddle:
                return False  # Ignore duplicate hits until ball moves away

            # Ball actually hit the paddle, register this as the last hit
            self.last_paddle_hit = paddle

            # Reflect ball
            self.setheading(180 - self.heading())

            # Determine direction
            self.ball_direction = "down" if self.ycor() < paddle.ycor() else "up"

            return True  # Collision detected

        # If ball has moved away from the last paddle, reset tracking
        if self.last_paddle_hit and abs(self.xcor() - self.last_paddle_hit.xcor()) > 50:
            self.last_paddle_hit = None

        return False

    # getter for ball direction
    def get_ball_direction(self):
        return self.ball_direction
    
   
