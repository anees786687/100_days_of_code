from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard


def freeze_game(message):
    """
    Freezes the game and displays a message.
    """
    screen.clear()  # Clear screen
    screen.bgcolor("black")  # Reset background

    # Display game over message
    game_over = Turtle()
    game_over.color("white")
    game_over.hideturtle()
    game_over.write(message, align="center", font=("Arial", 24, "bold"))

    screen.update()  # Show final state
    screen.mainloop()  # Freeze the game (wait for user to close window)


# Setting up screen
screen = Screen()
screen.setup(1000, 700)
screen.bgcolor("black")  # Set background color
screen.tracer(0)  # Disable automatic updates for smooth animation

# Setting up paddles
l_paddle = Paddle(x_value=-450, screen=screen)
r_paddle = Paddle(x_value=450, screen=screen)

# Setting up ball
ball = Ball()

# Setting up middle line
line = Turtle()
line.shape("square")
line.color("white")
line.penup()
line.setheading(90)  # Rotate upwards

# Draw the center line
line.goto(0, -screen.window_height()//2 + 20)  # Start near the bottom
while line.ycor() < screen.window_height()//2 + 20:
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

# Listen to key presses for paddles
screen.listen()
screen.onkeypress(l_paddle.move_up, "w")  # Move left paddle up with 'W'
screen.onkeypress(l_paddle.move_down, "s")  # Move left paddle down with 'S'
screen.onkeypress(r_paddle.move_up, "Up")  # Move right paddle up with 'Up'
screen.onkeypress(r_paddle.move_down, "Down")  # Move right paddle down with 'Down'


# setting up score board
disp_player_score = Scoreboard(-20,screen.window_height()//2 - 50)
disp_op_score = Scoreboard(20,screen.window_height()//2 - 50)
player_score = 0
ops_score = 0


# Function to run the game loop using `ontimer()`
def game_loop():
    global player_score
    global ops_score
    ball.move_ball()  # Move the ball
    screen.update()  # Refresh the screen
    # print(ball.heading())
    r_paddle.move_right_paddle(ball=ball)

    if ball.check_collision(r_paddle):
        ops_score += 1
        disp_op_score.update_score(ops_score)
    
    if ball.check_collision(l_paddle):
        player_score += 1
        disp_player_score.update_score(player_score)


    # Check if the ball is missed (Out of screen boundaries)
    if ball.xcor() > screen.window_width() // 2:
        freeze_game("Left Player Wins!")  # Right paddle missed
        
        return  # Stop the loop

    if ball.xcor() < -screen.window_width() // 2:
        freeze_game("Right Player Wins!")  # Left paddle missed
        return  # Stop the loop

    # print(f"Player: {player_score} Ops: {ops_score}")
    screen.ontimer(game_loop, 50)  # Call game_loop every 20ms for smooth movement
    

# Start the game loop
game_loop()

# Keep game running
screen.mainloop()
