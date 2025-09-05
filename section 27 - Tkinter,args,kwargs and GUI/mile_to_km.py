from tkinter import *

def miles_to_unit():
    """Convert miles to the selected unit with comprehensive conversion logic"""
    try:
        miles = float(miles_entry.get())
        selected_unit = km_label.cget('text')
        
        # Conversion factors from miles to different units
        conversions = {
            'Km': miles * 1.609344,        # Miles to kilometers
            'm': miles * 1609.344,         # Miles to meters  
            'cm': miles * 160934.4,        # Miles to centimeters
            'mm': miles * 1609344,         # Miles to millimeters
            'inches': miles * 63360,       # Miles to inches (1 mile = 63,360 inches)
            'feet': miles * 5280           # Miles to feet (1 mile = 5,280 feet)
        }
        
        if selected_unit in conversions:
            result = conversions[selected_unit]
            # Format result based on unit for better readability
            if selected_unit in ['cm', 'mm', 'inches']:
                km_val_label.config(text=f'{result:,.0f}')  # No decimals for large numbers
            else:
                km_val_label.config(text=f'{result:.3f}')   # 3 decimals for smaller numbers
        else:
            km_val_label.config(text='Invalid unit')
            
    except ValueError:
        km_val_label.config(text='Invalid input')
    except Exception as e:
        km_val_label.config(text='Error')

def listbox_used(event):
    """Handle listbox selection and update the unit label"""
    idx = unit_select_list.curselection()
    if idx:
        selection = unit_select_list.get(idx)
        km_label.config(text=selection)
        # Clear previous result when unit changes
        km_val_label.config(text='0')

def update_listbox_height():
    """Update listbox height based on number of items"""
    item_count = unit_select_list.size()
    # Set height to number of items, with a minimum of 2 and maximum of 6
    dynamic_height = max(2, min(item_count, 6))
    unit_select_list.config(height=dynamic_height)

def reset_converter():
    """Reset all fields to default values"""
    miles_entry.delete(0, END)
    km_val_label.config(text='0')
    km_label.config(text='Km')
    unit_select_list.selection_clear(0, END)
    unit_select_list.selection_set(0)  # Select first item (Km)

# Unit list with all supported conversions
unit_list = ['Km', 'm', 'cm', 'mm', 'inches', 'feet']

# Create main window
window = Tk()
window.title('Miles to Units Converter')
window.minsize(width=350, height=200)
window.config(padx=10, pady=10)

# Input section
miles_entry = Entry(width=10, justify='center', font=('Arial', 10))
miles_entry.grid(row=0, column=2, padx=5)
miles_entry.bind('<Return>', lambda event: miles_to_unit())  # Enter key triggers conversion

miles_label = Label(text='Miles', font=('Arial', 10))
miles_label.grid(row=0, column=3)

# Output section
eq_label = Label(text='is equivalent to', font=('Arial', 10))
eq_label.grid(row=1, column=0, columnspan=2, sticky='e', padx=5)

km_val_label = Label(text='0', font=('Arial', 10, 'bold'), fg='blue')
km_val_label.grid(row=1, column=2, padx=5)

km_label = Label(text='Km', font=('Arial', 10))
km_label.grid(row=1, column=3)

# Control buttons
calc_button = Button(
    text='Calculate', 
    command=miles_to_unit,
    bg='lightgreen',
    font=('Arial', 9),
    width=10
)
calc_button.grid(row=2, column=1, pady=5)

reset_button = Button(
    text='Reset', 
    command=reset_converter,
    bg='lightcoral',
    font=('Arial', 9),
    width=10
)
reset_button.grid(row=2, column=2, pady=5)

# Unit selection section
unit_label = Label(text='Select unit:', font=('Arial', 9))
unit_label.grid(row=3, column=0, sticky='e', padx=5, pady=(10, 0))

unit_select_list = Listbox(
    font=('Arial', 9),
    selectmode='single',
    exportselection=False  # Prevents selection from being cleared when clicking elsewhere
)

# Add items to listbox
for index, unit in enumerate(unit_list):
    unit_select_list.insert(index, unit)

# Set default selection to first item (Km)
unit_select_list.selection_set(0)

# Update height based on number of items
update_listbox_height()

unit_select_list.bind('<<ListboxSelect>>', listbox_used)
unit_select_list.grid(row=3, column=1, columnspan=2, pady=(10, 0), sticky='w')

# Instructions
instructions = Label(
    text='Enter miles, select unit, and click Calculate',
    font=('Arial', 8),
    fg='gray'
)
instructions.grid(row=4, column=0, columnspan=4, pady=(10, 0))

window.mainloop()