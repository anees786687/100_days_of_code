import turtle as t
from paddle import Paddle
from ball import Ball
class Player(Paddle):
    PADDLE_Y = 0
    def __init__(self, screen: t.Screen, ball: Ball):
        super().__init__(screen, ball)
        self.screen = screen
        self.paddle_x = -self.screen.window_width() // 2 + 2 * Paddle.PADDLE_WIDTH
        self.teleport(x=self.paddle_x, y = Player.PADDLE_Y)
        self.direction = None
        self.score = 0
        self.player_win = False
        
    def move_up(self):
        # self.check_ball_collision()
        if self.check_boundary_collision() and self.direction == 'up':
            self.fd(0)
        else:
            self.fd(10)
            self.direction = 'up'

    def move_down(self):
        if self.check_boundary_collision() and self.direction == 'down':
            self.bk(0)
        else:
            self.bk(10)
            self.direction = 'down'

    def player_score(self):
        if self.check_ball_collision() and self.ball.xcor() < self.xcor() + self.PADDLE_WIDTH // 2:
            # this means that the ball is toward the side of the player and has collided with the player paddle
            self.score+=1
        # check the state of ball collision and check once the ball is in the opps x range then make
        # collision false
        if self.get_ball_collision_state() and self.ball.xcor() > 0:
            self.change_ball_collision_state()

    def set_player_win(self):
        self.player_win = True

    def get_player_win(self):
        return self.player_win
    
    def get_player_score(self):
        return self.score

   
