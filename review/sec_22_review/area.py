import turtle as t
from player import Player
from opps import Opps

class Area(t.Turtle):
    def __init__(self, screen: t.Screen, player: Player, opps: Opps):
        super().__init__()
        self.screen = screen
        self.player = player
        self.opps = opps
        self.line = t.Turtle()
        self.line.color('white','white')
        self.line.setheading(270)
        self.line.teleport(y=self.screen.window_height() // 2)
        
        # draw dotted line
        while self.line.ycor() > -self.screen.window_height() // 2:
            self.line.fd(10)
            self.line.penup()
            self.line.fd(10)
            self.line.pendown()

        self.opps_score = 0
        self.player_score = 0

        self.opps_scorer = t.Turtle()
        self.opps_scorer.teleport(x=20, y = self.screen.window_height() // 2.25)
        self.opps_scorer.color('white','white')
        self.opps_scorer.write(f'{self.opps_score}', font=('Arial', 24, 'normal'))
        self.opps_scorer.hideturtle()


        self.player_scorer = t.Turtle()
        self.player_scorer.teleport(x=-40, y = self.screen.window_height() // 2.25)
        self.player_scorer.color('white','white')
        self.player_scorer.write(f'{self.player_score}', font=('Arial', 24, 'normal'))
        self.player_scorer.hideturtle()

        self.game_over_writer = t.Turtle()
        self.game_over_writer.teleport(-150,0)
        self.game_over_writer.color('white','white')
        self.game_over_writer.hideturtle()
  


    def update_score(self):
        player_temp = self.player.get_player_score()
        if  player_temp > self.player_score:
            self.player_score = player_temp
            self.player_scorer.clear()
            self.player_scorer.write(f'{self.player_score}', font=('Arial', 24, 'normal'))

        opps_temp = self.opps.get_opps_score()
        if opps_temp > self.opps_score:
            self.opps_score = opps_temp
            self.opps_scorer.clear()
            self.opps_scorer.write(f'{self.opps_score}', font=('Arial', 24, 'normal'))
    
    def write_game_over(self, msg: str):
        self.game_over_writer.write(f'Game Over {msg} wins',  font=('Arial', 24, 'normal'))