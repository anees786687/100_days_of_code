"""Building a turtle race game

1. start by creating multiple turltle objects with variosu colors and move them to the start line

2. Get the name of the turtle you wanna bet on

3. start the race
"""
import turtle as t
import random as r


# 1. multiple turtles and moving them to start line
## create a list of colors 
color_list = ['purple','blue','green','yellow','orange','red']
screen = t.Screen()
screen.setup(width=500, height=400)
turtle_list = []
turt_x = -240
turt_y = -150
for i in range(0,len(color_list)):
    temp_turt = t.Turtle()
    temp_turt.shape('turtle')
    temp_turt.fillcolor(color_list[i])
    temp_turt.teleport(turt_x, turt_y)
    temp_turt.penup()
    turt_y += 60
    turtle_list.append(temp_turt)

# 2. Get the name of the turtle you wanna bet on
while True:
    bet_turtle = screen.textinput(title='bet_it', prompt='Enter the color of the turtle to bet on')

    if bet_turtle.lower() in color_list:
        break

    print('Turtle name not in the list, try again!')

print(f'You bet on {bet_turtle} turtle')

#3. start the race
winning_turt = None
while True:
    for turt in turtle_list:
        turt: t.Turtle  # Type hint to help IDE recognize the type
        turt.fd(r.randint(10,30))

        if(turt.xcor() > screen.window_width() // 2 - 20):
            winning_turt = turt
            break

    if winning_turt != None:
        break

winning_color = winning_turt.color()[1]
if winning_color == bet_turtle:
    print(f'{bet_turtle} turtle has won. Congrats!')
else:
    print(f'Wah wah! {winning_color} tutle won')

screen.exitonclick()