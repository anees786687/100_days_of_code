import pandas as pd
import turtle as t
from PIL import Image

img = Image.open('./blank_states_img.gif')
width, height = img.size
# 725, 491
print(width, height)
states = pd.read_csv('./50_states.csv')
state_list = states.state.to_list()
state_x = states.x.to_list()
state_y = states.y.to_list()
guessed_states = []
unguessed_states = None
# print(state_list)
screen = t.Screen()
screen.screensize(canvwidth=width,canvheight=height)
screen.bgpic('./blank_states_img.gif') # set the background of the screen as the map
writer_turt = t.Turtle() # this turtle will write the name of the state at some (x,y)
writer_turt.hideturtle()
warning_turt = t.Turtle()
warning_turt.hideturtle()



"""
game loop logic

1. give prompt to user
2. user enters prompt
3. check if the state is in the list
3.1 if yes goto 4
3.2 else goto 2
4. write the name of the state at the respective (x,y)
5. goto 1
"""
game_state = True
while game_state:
    state = None
    # global unguessed_states
    guess = screen.textinput('User Input', 'Enter the name of the state').title()
    # print(guess)
    if guess.lower() == 'exit':
        game_state = False  
    elif guess not in state_list:
        if guess == None:
            pass
        elif guess in guessed_states:
            warning_turt.clear()
            warning_turt.penup()
            warning_turt.goto(0.0, screen.window_height() / 3)
            warning_turt.pendown()
            warning_turt.write(f'Already guessed {guess}', align='center', font=('Arial', 20, 'normal'))
        else:    
            warning_turt.penup()
            warning_turt.goto(0.0, screen.window_height() / 3)
            warning_turt.pendown()
            warning_turt.write(f'No state names {guess}', align='center', font=('Arial', 20, 'normal'))
    else:
        state_index = state_list.index(guess)
        x_val = state_x[state_index]
        y_val = state_y[state_index]
        warning_turt.clear()

        writer_turt.penup()
        writer_turt.goto(x_val,y_val)
        writer_turt.pendown()
        writer_turt.write(f'{guess}', align='center', font=('Arial', 10, 'normal'))
        guessed_states.append(guess)
        


unguessed_states = [state for state in state_list if state not in guessed_states]
print(unguessed_states)
save_file_dict = {
    "remaining states": unguessed_states
}
remaing_state_df = pd.DataFrame(save_file_dict)
print(remaing_state_df)
remaing_state_df.to_csv('./remaining_states.csv')
screen.mainloop()