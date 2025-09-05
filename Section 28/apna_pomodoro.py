from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECS = 60

reset_pressed = False
long_berak_over = False
check_count = 0
state = 'work'
# ✓ 25 -> 5 -> 25 -> 5 -> 25 -> 5 -> 25 -> 20
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer(window: Tk, canvas: Canvas, id):
    global reset_pressed
    reset_pressed = True
    canvas.itemconfig(id,text=f'{WORK_MIN}:00')
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(window: Tk, canvas: Canvas, id, set_time, secs):
    global reset_pressed
    global check_count
    global state
    global long_berak_over
    if secs == 0:
        set_time-=1
        secs = SECS
    secs-=1

   
    if set_time == 0 and secs == 0 or reset_pressed:
        if state == 'work':
            check_count += 1
            check_label.config(text=f'✓' * check_count)
            if check_count == 4:
                state = 'long break'
            else:
                state = 'short break'
        elif state == 'long break':
            long_berak_over = True
            state = 'work'
        else:
            state = 'work'
            
        if reset_pressed: # if button is pressed, reset everything and go back to work state
            check_count = 0
            check_label.config(text='')
            state = 'work'
            window.after_cancel(id)
            reset_pressed = False
            long_berak_over = False
            return
        elif state == 'long break': # post long break go into work state
            print('long')
            set_time = LONG_BREAK_MIN
        elif state == 'work':
            if long_berak_over:
                check_count = 0 # reset the counter
                check_label.config(text="")
                long_berak_over = False

            set_time = WORK_MIN
            # start break timer
            print('work mode', check_count)
        elif state == 'short break': # 
            set_time = SHORT_BREAK_MIN
            print('short')

    
    text = f'{set_time}:{secs}' if secs >= 10 else  f'{set_time}:0{secs}'
    canvas.itemconfig(timer_id,text=text)
    window.after(1000, lambda: start_timer(window, canvas, id, set_time, secs))
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.minsize(width=700, height=700)
# rather than specifying the size of window one can use padx and pady to align components
# to desired position
window.config(padx=100, pady=50,bg=YELLOW)
window.title('Pomodoro!')
"""To put images, we have to learn about canvas. Canvas allows you to layer things
on top of one another, so we can add an image to the canvas and then add something on that 
image"""
# creating a canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# adding image to canvas, we cant directly add an image. To add an image 
# we have to use a a PhotoImage object, this is class that comes from tkinter and is 
# a way to read through the file and get hold of a paticular image
pi = PhotoImage(file='./tomato.png')
canvas.create_image(100,112,image=pi)
timer_id = canvas.create_text(103,130,text=f'{WORK_MIN}:00', fill='white', font=(FONT_NAME,30, "bold"))
print(timer_id)
canvas.grid(row=1, column=1)


timer_lable = Label(text='Timer', font=(FONT_NAME, 32,'normal'),fg=GREEN, bg=YELLOW)
timer_lable.grid(row=0, column=1)

start_button = Button(text='Start', anchor='center', command=lambda:start_timer(window, canvas, timer_id, WORK_MIN, 0))
start_button.grid(row=2,column=0)

reset_button = Button(text='Reset', anchor='center', command=lambda:reset_timer(window, canvas,timer_id))
reset_button.grid(row=2, column=2)

check_label = Label(text='✓' * check_count, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'normal'))
check_label.grid(row=2, column=1)

print('work')
window.mainloop()