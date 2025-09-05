import turtle as t
from paddle import Paddle
from player import Player
from opps import Opps
from ball import Ball
from area import Area
import time

screen = t.Screen()
screen.setup(width=1000, height=750)
screen.bgcolor('black')
screen.tracer(0)
ball = Ball(screen)
player = Player(screen, ball)
opps = Opps(screen, ball)
area = Area(screen=screen,player=player,opps=opps)


screen.onkeypress(player.move_up,'Up')
screen.onkeypress(player.move_down,'Down')
screen.listen()

"""
setup the paddle - done
setup player paddle, this paddle will have functionality to move up and down
setup opponent paddle, define a simple p controller to move the paddle in the correct y direction of the ball.

setup ball, ball will check collisions with the paddles and the boundries

setup screen, draw a dashed line in the center and keep a score, given message if player or opps win
"""

def game_loop():
    opps.move_opps_paddle()
    # player.check_ball_collision()
    # opps.check_ball_collision()
    ball.play_ball()

    player.player_score()
    opps.opp_score()

    if ball.ball_oob():
        if ball.xcor() > 0:
            player.set_player_win()
        elif ball.xcor() < 0:
            opps.set_opps_win()

    if player.get_player_win():
        area.write_game_over('Player')
        return  # Exit function - game stops here
    elif opps.get_opps_win():
        area.write_game_over('Opps')
        return  # Exit function - game stops here

    area.update_score()
    screen.update()
    screen.ontimer(game_loop, 50)  # Continue game loop

game_loop()

screen.exitonclick()