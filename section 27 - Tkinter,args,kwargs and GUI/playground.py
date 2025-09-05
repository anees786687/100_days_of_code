from tkinter import *

window = Tk()
window.minsize(width=300,height=300)

# to add padding to window
window.config(padx=20,pady=20)

label = Label(text='my_label')
label.grid(row=0,column=0)
# to add padding to a component
label.config(padx=10,pady=10)

button_1 = Button(text='button_1')
button_1.grid(row=1,column=1)

button_2 = Button(text='button_2')
button_2.grid(row=0, column=2)

entry = Entry(width=10)
entry.grid(row=2,column=3)

window.mainloop()