from tkinter import *

def get_label_values():
    """Function to demonstrate getting label values"""
    
    # Method 1: Using cget() method (Recommended)
    label_text = my_label.cget('text')
    print(f"Label text using cget(): {label_text}")
    
    # Method 2: Using dictionary-style access
    label_text_dict = my_label['text']
    print(f"Label text using dict access: {label_text_dict}")
    
    # Get other label properties
    label_font = my_label.cget('font')
    label_fg = my_label.cget('fg')
    label_bg = my_label.cget('bg')
    
    print(f"Font: {label_font}")
    print(f"Foreground color: {label_fg}")
    print(f"Background color: {label_bg}")
    
    # Update the info label with current values
    info_text = f"Current label text: '{label_text}'"
    info_label.config(text=info_text)

def change_label_text():
    """Change the label text to demonstrate value retrieval"""
    new_text = entry.get()
    if new_text:
        my_label.config(text=new_text)
        entry.delete(0, END)  # Clear the entry field

# Create main window
window = Tk()
window.title('Get Label Value Example')
window.minsize(width=400, height=250)
window.config(padx=20, pady=20)

# Create the main label
my_label = Label(
    text='Hello, Tkinter!',
    font=('Arial', 14, 'bold'),
    fg='blue',
    bg='lightgray',
    padx=10,
    pady=5
)
my_label.grid(row=0, column=0, columnspan=2, pady=10)

# Entry to change label text
Label(text='New text:').grid(row=1, column=0, sticky='e', padx=5)
entry = Entry(width=20)
entry.grid(row=1, column=1, padx=5)

# Button to change label text
change_button = Button(
    text='Change Label Text',
    command=change_label_text,
    bg='lightgreen'
)
change_button.grid(row=2, column=0, columnspan=2, pady=5)

# Button to get label values
get_values_button = Button(
    text='Get Label Values',
    command=get_label_values,
    bg='lightblue'
)
get_values_button.grid(row=3, column=0, columnspan=2, pady=5)

# Info label to display current values
info_label = Label(
    text='Click "Get Label Values" to see current text',
    font=('Arial', 10),
    fg='gray'
)
info_label.grid(row=4, column=0, columnspan=2, pady=10)

# Instructions
instructions = Label(
    text='Instructions:\n1. Change the text in the entry field\n2. Click "Change Label Text"\n3. Click "Get Label Values" to see the current text',
    font=('Arial', 9),
    justify='left',
    bg='lightyellow',
    padx=10,
    pady=5
)
instructions.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
