"""
Tkinter GUI Programming - Complete Widget Examples

This module demonstrates various Tkinter widgets and their usage.
Tkinter is Python's standard GUI (Graphical User Interface) toolkit.

Key Concepts:
1. Window Creation - Using Tk() to create the main window
2. Widget Creation - Labels, Buttons, Entry fields, etc.
3. Widget Configuration - Setting properties like colors, fonts, sizes
4. Event Handling - Responding to user interactions
5. Layout Management - Using pack() to arrange widgets

Resources:
- Official Tkinter docs: https://docs.python.org/3/library/tkinter.html
- Packer documentation: https://www.tcl-lang.org/man/tcl8.6/TkCmd/pack.htm
"""

import tkinter as tk
from tkinter import END, IntVar

# ============================================================================
# WINDOW CREATION AND CONFIGURATION
# ============================================================================

# Create the main application window
window = tk.Tk()  # This creates the root window (equivalent to screen in turtle graphics)

# Configure window properties
window.title('Tkinter Widget Demonstration')  # Set the window title
window.minsize(width=500, height=300)  # Set minimum window size (can be resized larger)

# ============================================================================
# LABELS - Display text or images
# ============================================================================

# Create a label widget
my_label = tk.Label(
    text='I am a label',  # The text to display
    font=('Arial', 10, 'normal')  # Font: (family, size, style)
)

# Display the label using the pack geometry manager
my_label.pack()  # REQUIRED: Without pack(), the widget won't be visible

# Method 1: Configure widget properties using dictionary-style syntax
my_label['fg'] = 'blue'  # Set foreground (text) color

# Method 2: Configure widget properties using the config() method
my_label.config(
    background='green',  # Set background color
    bd=5  # Set border width (bd is short for borderwidth)
)

# ============================================================================
# BUTTONS - Clickable widgets that trigger actions
# ============================================================================

# Define callback function for button click events
def button_click():
    """
    This function is called when the button is clicked.
    It updates the label text with whatever is in the entry field.
    """
    new_text = entry.get()  # Get text from the entry widget
    my_label.configure(text=new_text)  # Update the label's text
    print(f"Button clicked! Entry text: {new_text}")

# Create a button widget
button = tk.Button(
    text='Press Me',  # Button text
    font=('Times New Roman', 15),  # Font configuration
    foreground='red',  # Text color
    activebackground='black',  # Background color when button is pressed
    activeforeground='red',  # Text color when button is pressed
    command=button_click  # Function to call when button is clicked
)
button.pack()

# ============================================================================
# ENTRY - Single-line text input
# ============================================================================

# Create an entry widget for single-line text input
entry = tk.Entry()
entry.configure(width=30)  # Set the width in characters
entry.insert(0, 'Enter email here')  # Insert placeholder text at position 0
entry.pack()

# ============================================================================
# TEXT - Multi-line text input/display
# ============================================================================

# Create a text widget for multi-line text input
text = tk.Text(
    height=5,  # Height in lines
    width=30   # Width in characters
)
text.focus()  # Set keyboard focus to this widget when program starts
text.insert('1.0', "Multi-line text widget\nYou can type here")  # Insert text at line 1, character 0
text.pack()

# ============================================================================
# SPINBOX - Numeric input with up/down arrows
# ============================================================================

def spinbox_used():
    """Callback function for spinbox value changes"""
    value = spinbox.get()
    print(f"Spinbox value: {value}")

# Create a spinbox for numeric input
spinbox = tk.Spinbox(
    from_=0,  # Minimum value
    to=10,    # Maximum value
    width=5,  # Width in characters
    command=spinbox_used  # Function to call when value changes
)
spinbox.pack()

# ============================================================================
# SCALE - Slider widget for selecting values from a range
# ============================================================================

def scale_used(value):
    """
    Callback function for scale widget.
    Note: The scale automatically passes its current value as an argument.
    """
    print(f"Scale value: {value}")

# Create a scale (slider) widget
scale = tk.Scale(
    from_=0,        # Minimum value
    to=10,          # Maximum value
    orient='horizontal',  # Can be 'horizontal' or 'vertical'
    command=scale_used,   # Function to call when value changes
    digits=5,       # Total number of digits to display
    resolution=0.001  # Smallest increment
)
scale.pack()

# ============================================================================
# CHECKBUTTON - Binary choice widget (checked/unchecked)
# ============================================================================

def checkbutton_used():
    """Callback function for checkbutton state changes"""
    is_checked = check_var.get()  # Returns 1 if checked, 0 if unchecked
    status = "checked" if is_checked else "unchecked"
    print(f"Checkbutton is {status}")

# Create a variable to store checkbutton state
check_var = IntVar()  # IntVar stores integer values (0 or 1 for checkbuttons)

# Create checkbutton widget
check_button = tk.Checkbutton(
    text='Is this option enabled?',  # Display text
    variable=check_var,              # Variable to store the state
    command=checkbutton_used         # Function to call when state changes
)
check_button.pack()

# ============================================================================
# RADIOBUTTONS - Multiple choice widget (only one can be selected)
# ============================================================================

def radio_used():
    """Callback function for radiobutton selection changes"""
    selected_value = radio_var.get()
    print(f"Selected option: {selected_value}")

# Create a variable to store which radiobutton is selected
radio_var = IntVar()  # All radiobuttons sharing this variable form a group

# Create multiple radiobuttons that share the same variable
radio_button_1 = tk.Radiobutton(
    text='Option 1',        # Display text
    value=1,                # Value stored when this button is selected
    variable=radio_var,     # Shared variable
    command=radio_used      # Function to call when selection changes
)

radio_button_2 = tk.Radiobutton(
    text='Option 2',
    value=2,
    variable=radio_var,
    command=radio_used
)

# Pack both radiobuttons
radio_button_1.pack()
radio_button_2.pack()

# ============================================================================
# LISTBOX - Widget for displaying and selecting from a list of items
# ============================================================================

def listbox_used(event):
    """
    Callback function for listbox selection changes.
    Note: Listbox events pass an event object as parameter.
    """
    try:
        # Get the selected item(s)
        selection_indices = listbox.curselection()  # Returns tuple of selected indices
        if selection_indices:  # Check if anything is selected
            selected_item = listbox.get(selection_indices[0])  # Get first selected item
            print(f"Selected item: {selected_item}")
    except IndexError:
        print("No item selected")

# Create a listbox widget
listbox = tk.Listbox(height=4)  # Height in number of visible items

# Add items to the listbox
fruits = ['Apple', 'Pear', 'Banana', 'Orange']
for index, fruit in enumerate(fruits):
    listbox.insert(index, fruit)  # Insert item at specific index

# Bind the selection event to our callback function
listbox.bind('<<ListboxSelect>>', listbox_used)  # Special event for listbox selection
listbox.pack()


# Layout manager
"""
3 types - 

1. pack - basically pakcs widget next to each other in a vaguely logical format
by default pack starts from top and packs widgets below the before one.

Problem with pack is it is diffcult to provide specific position to place the component

2. Place: all abut precise positioning, can provide specific x,y value, it uses the width and 
height of the window to place the component. Downside is that its too speciifc and e have to wrkout 
in our head where to place, this is an issue when there are too many components

3. grid - very simple concept, imagines entire window is grid and we can define the number of 
columns and rows, we have to provide a column and a row number (both start from 0), grid system is relative 
to other component. So the easiest way of working with the grid is starting with the things that you want it to be at the top left,
defining a starting column and rows, zero, zero, and then for the next and subsequent widgets to just keep going through it and
define its position on the grid.

YOU CANT MIX GRID AND PACK IN THE SAME PROGRAM, THIS WILL GIVE AN ERROR!!!!

example in playground.py
"""
# ============================================================================
# EVENT LOOP - Keep the window running and responsive
# ============================================================================

# Start the main event loop
# This MUST be the last line in your GUI program
# It keeps the window open and listens for user interactions
window.mainloop()