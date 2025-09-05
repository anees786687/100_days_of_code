from turtle import Screen, Turtle
import random
# tim = Turtle("turtle")
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Name", "Enter the name of the turtle you want to bet on")
is_race_on = False

"""
Maintain a list of turtle colors and their coords, this will help us to make a list of
turtle objects.
"""
players = []
colors = ["red","orange", "yellow", "green", "blue", "purple"]
coords = [(-230,100),(-230,60),(-230,20),(-230,-20),(-230,-60),(-230,-100)]
for i in range(0,6):
    turt = Turtle("turtle")
    turt.color(colors[i])
    players.append(turt)
    # turt.speed(1)
    turt.penup()
    turt.goto(coords[i])


"""
Now we have to make a random turtle move random step until one of the turtle reaches the finish line
we ensure that the race starts when the bet is places, post that we iterate through the list and move each 
turtle by random integer values between [0,10]. Once one of the turtle has reached the finish line, the game 
checks which turtle has won, displays the result and finihes the race.
"""
if user_bet:
    is_race_on = True

while is_race_on:
    for i,turt in enumerate(players):
        rand_dist = random.randint(0,10)
        turt.fd(rand_dist)
        if turt.xcor() >= float(screen.window_width()/2 - 20):
            if colors[i] == user_bet:
                print("You Won")
            else:
                print(f"You Lose {colors[i]} turtle won")

            is_race_on = False
            break

screen.exitonclick()