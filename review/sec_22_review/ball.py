import turtle as t
import random

class Ball(t.Turtle):
    def __init__(self, screen: t.Screen):
        super().__init__()
        self.screen = screen
        # t.mode('standard') # ccw angles are positive
        self.shape('circle')
        self.color('white','white')
        self.ball_range = random.choice(((45,60),(-60,-45),(120,135),(-135,-120)))
        self.setheading(random.choice(self.ball_range))
        self.penup()
        # self.setheading(330)
        
        # self.setheading(180)

        self.ball_direction = None

    def set_ball_direction(self):
        if self.heading() > 0.0 and self.heading() < 180.0:
            self.ball_direction = 'up'
        else:
            self.ball_direction = 'down'

    def play_ball(self):
        self.set_ball_direction()
        self.detect_collison()
 
        self.fd(10)

    def detect_collison(self):
        """
        For collision with paddle

        conside the center point of the paddle and the center point of the ball,
        apply distance formula and check if the distance between the two points is less than 54 pixels (calculated from pythogorus theorem)
        then take the current angle subtract it by 180 and then set the se
        """
        # first we set collision with the boundary
        if abs(self.ycor()) > self.screen.window_height() // 2 - 10:
            self.setheading(360 - self.heading())

    def ball_oob(self):
        
        if abs(self.xcor()) > self.screen.window_width() // 2:
            return True
        return False
    


        

