import tkinter as tk


window = tk.Tk()
window.title('my title')
window.minsize(width=500, height=300)

my_label = tk.Label(text='my label', font=('Arial',24,'bold'))

"""
The pack method has something called defualt arguements, for example, if side is not mentioned then there is a default value to it

this can be done by giving values to arguements while creating the function

def func(a=2,b=3,c=4):
    pass
    
we can override the default arguements too
func(b=10) will override the value of b but the value of a and c will remain the same
"""
my_label.pack(side='left')

window.mainloop()