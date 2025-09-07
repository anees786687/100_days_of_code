"""
Password Manager GUI Application

A secure password manager with real-time validation and password generation.
Features:
- Real-time input validation for websites, emails, and passwords
- Automatic password generation
- Data persistence to JSON file
- User-friendly GUI with visual feedback
- Search functionality for existing entries

Author: Anees Alwani
Date: 5th September 2025
"""

from tkinter import *
from tkinter import messagebox # Importing message box, the first line doesn't implement modules but all the classes
import random as r
import os
import re  # For regex pattern matching
import json

class PassWordGen:
    """
    Main Password Manager class that handles GUI creation, validation, and data storage.
    """
    
    def __init__(self):
        """Initialize the application window and validation state variables."""
        self.window = Tk()
        
        # Validation state flags - track if each field is valid
        self.email_good = False
        self.url_good = False
        self.pass_good = False
        
        # Data storage variables
        self.username = None
        self.email = None
        self.website = None
        self.passwd = None

        # Dictionary to hold JSON data for file operations
        self.json_deets = {}
        self.init_ui()
    
    def init_ui(self):
        """Initialize and configure the user interface components."""
        # Configure main window properties
        self.window.config(padx=40, pady=40)
        self.window.title('Password Manager')

        # --- Logo Section ---
        # Create frame for logo/image display
        self.img_frame = Frame(self.window)
        self.img_frame.grid(row=0, column=0, pady=(0, 20))
        
        # Canvas widget for displaying the logo image
        self.canvas = Canvas(self.img_frame, width=200, height=190, highlightthickness=0)
        
        try:
            # Attempt to load and display logo image
            img_path = os.path.join(os.path.dirname(__file__), './logo.png')
            self.logo = PhotoImage(file=img_path)
            self.canvas.create_image(100, 95, image=self.logo)  # Centered positioning
        except Exception as e:
            # Handle case where logo file is missing or corrupted
            print(f'Error while fetching image: {e}')
        
        self.canvas.grid(row=0, column=0)

        # --- Main Data Entry Frame ---
        # Container frame for all input fields
        self.data_frame = Frame(self.window)
        self.data_frame.grid(row=1, column=0, sticky='ew')

        # --- Website URL Input Section ---
        self.website_frame = Frame(self.data_frame)
        self.website_frame.grid(row=0, column=0, pady=5, sticky='ew')
        
        # Website label with consistent styling
        self.website_label = Label(self.website_frame, text='Website:', font=('Arial', 13), width=15, anchor='e')
        self.website_label.grid(row=0, column=0, padx=(0, 10), sticky='e')
        
        # Website entry field with visual styling and validation
        self.website_entry = Entry(
            self.website_frame,
            width=30,
            font=('Arial', 10),
            highlightthickness=2,
            highlightcolor='blue'
        )
        self.website_entry.grid(row=0, column=1, sticky='w')
        
        # Bind real-time validation to keystrokes
        self.website_entry.bind('<KeyRelease>', lambda event: self.check_url(self.website_entry.get()))
        
        # Validation feedback label for website field
        self.website_valid_info = Label(self.website_frame, text="", fg="red", font=('Arial', 10))
        self.website_valid_info.grid(row=0, column=2, sticky='w')

        # Search button for finding existing website entries
        self.search_button = Button(self.website_frame, text='Search', command=self.search_details, width=15)
        self.search_button.grid(row=0, column=2, sticky='w', padx=(5, 0))
        
        # --- Email Input Section ---
        self.email_frame = Frame(self.data_frame)
        self.email_frame.grid(row=1, column=0, pady=5, sticky='ew')
        
        # Email label with consistent styling
        self.email_label = Label(self.email_frame, text='Email:', font=('Arial', 13), width=15, anchor='e')
        self.email_label.grid(row=0, column=0, padx=(0, 10), sticky='e')
        
        # Email entry field with validation styling
        self.email_entry = Entry(
            self.email_frame,
            width=30,
            font=('Arial', 10),
            highlightthickness=2,
            highlightcolor='blue'
        )
        self.email_entry.grid(row=0, column=1, sticky='w')
        
        # Real-time email validation on every keystroke
        self.email_entry.bind('<KeyRelease>', lambda event: self.check_email(self.email_entry.get()))
        
        # Email validation feedback label
        self.email_valid_info = Label(self.email_frame, text="", fg="red", font=('Arial', 10))
        self.email_valid_info.grid(row=0, column=2, sticky='w')

        # --- Username Input Section (Optional) ---
        self.username_frame = Frame(self.data_frame)
        self.username_frame.grid(row=2, column=0, pady=5, sticky='ew')
        
        # Username label with multi-line text for clarity
        self.username_label = Label(self.username_frame, text='Username\n(if applicable):', font=('Arial', 13), width=15, anchor='e')
        self.username_label.grid(row=0, column=0, padx=(0, 10), sticky='e')
        
        # Optional username entry field
        self.username_entry = Entry(
            self.username_frame,
            width=30,
            font=('Arial', 10),
            highlightthickness=2,
            highlightcolor='blue',
        )
        self.username_entry.grid(row=0, column=1, sticky='w', padx=(0, 5))

        # --- Password Input Section ---
        self.pass_frame = Frame(self.data_frame)
        self.pass_frame.grid(row=3, column=0, pady=5, sticky='ew')
        
        # Password label with consistent styling
        self.pass_label = Label(self.pass_frame, text='Password:', font=('Arial', 13), width=15, anchor='e')
        self.pass_label.grid(row=0, column=0, padx=(0, 10), sticky='e')
        
        # Password entry field with validation styling
        self.pass_entry = Entry(
            self.pass_frame,
            width=30,
            font=('Arial', 10),
            highlightthickness=2,
            highlightcolor='blue'
        )
        self.pass_entry.grid(row=0, column=1, sticky='w', padx=(0, 5))
        
        # Real-time password validation on every keystroke
        self.pass_entry.bind('<KeyRelease>', lambda event: self.check_pass(self.pass_entry.get()))
        
        # Password validation feedback label
        self.pass_valid_info = Label(self.pass_frame, text="", fg="red", font=('Arial', 10))
        self.pass_valid_info.grid(row=1, column=1, sticky='ew')
        
        # Button to auto-generate secure password
        self.gen_pass_button = Button(self.pass_frame, text='Generate Password', width=15, command=self.gen_pass)
        self.gen_pass_button.grid(row=0, column=2, sticky='w')
        
        # --- Save Data Button ---
        self.add_button_frame = Frame(self.data_frame)
        self.add_button_frame.grid(row=4, column=0, pady=5, sticky='ew')
        
        # Main button to save all entered data
        self.add_button = Button(self.add_button_frame, text='Add', width=30, justify='center', command=self.get_deets)
        self.add_button.grid(row=0, column=1, columnspan=2, sticky='e', padx=(150, 0))
    
    def search_details(self):
        """
        Search for existing website entries in the JSON file.
        Displays found credentials in a message box.
        """
        # Get the website name from the entry field
        website_name = self.website_entry.get()
        
        try:
            # Attempt to open and read the JSON file
            with open('./passwords.json', 'r') as f:
                data = json.load(f)
            
            # Try to find the website in the data
            details: dict = data.get(website_name)
            if details is None:
                # Website not found in the file
                raise KeyError()
            
            # Display found credentials in a message box
            messagebox.showinfo(title='Login Info', \
                                message=f"Email: {details.get('email')}\nPassword: {details.get('password')}\nUsername: {details.get('username')}")
        except FileNotFoundError:
            # Handle case where JSON file doesn't exist yet
            messagebox.showerror(title='Error!', message='File not found! Please make an entry to create the file!')
            return
        except KeyError:
            # Handle case where website is not found in existing data
            messagebox.showerror(title='Error!', message='No such entry for the website!')
            return

    def get_deets(self):
        """
        Collect and save user input data to JSON file.
        Only saves if all required fields are valid.
        """
        # Get and clean input data from all fields
        self.website = self.website_entry.get().strip()
        self.username = self.username_entry.get().strip() if self.username_entry.get() != "" else None
        self.email = self.email_entry.get().strip()
        self.passwd = self.pass_entry.get().strip()

        # Validate that website field is not empty
        if self.url_good == False:
            messagebox.showerror(title='Error', message='Please enter a name for the website!')
            return
        # Only proceed if all validations pass
        elif self.email_good and self.pass_good and self.url_good:
            # Reset validation flags after successful save
            self.email_good = False
            self.pass_good = False
            self.url_good = False

            # Clear all input fields after saving
            self.website_entry.delete(0, len(self.website))
            self.website_entry.config(highlightthickness=0)

            # Clear username field if it was used
            if self.username:
                self.username_entry.delete(0, len(self.username))
                self.username_entry.config(highlightthickness=0)
            
            # Clear email field and reset its validation display
            self.email_entry.delete(0, len(self.email))
            self.email_entry.config(highlightthickness=0)
            self.email_valid_info.config(text="")

            # Clear password field and reset its validation display
            self.pass_entry.delete(0, len(self.passwd))
            self.pass_entry.config(highlightthickness=0)
            self.pass_valid_info.config(text="")

            # Save to JSON file with proper error handling
            try:
                # Try to open existing file and load current data
                with open('./passwords.json', mode='r') as file:
                    self.json_deets = json.load(file)

                # Create new entry object based on whether username is provided
                new_json_obj = {
                    self.website: {
                        "email": self.email,
                        "password": self.passwd
                    }
                } if not self.username else {
                    self.website: {
                        "email": self.email,
                        "username": self.username,
                        "password": self.passwd
                    }
                }
                # Update existing data with new entry
                self.json_deets.update(new_json_obj)
               
            except FileNotFoundError:
                # If file doesn't exist, create new data structure
                new_json_obj = {
                    self.website: {
                        "email": self.email,
                        "password": self.passwd
                    }
                } if not self.username else {
                    self.website: {
                        "email": self.email,
                        "username": self.username,
                        "password": self.passwd
                    }
                }
                # Initialize json_deets with the new entry
                self.json_deets.update(new_json_obj)
                messagebox.showinfo(title='Info', message='Creating new password file!')
            finally:
                # Always write the data to file (either updated or new)
                with open('./passwords.json', mode='w') as file:
                    json.dump(self.json_deets, file, indent=4)
                    messagebox.showinfo(title="Success!", message='Details successfully stored')

                # Clear the in-memory data after saving
                self.json_deets = {}

    def gen_pass(self):
        """
        Generate a secure random password with mixed character types.
        Automatically populates the password field and validates it.
        """
        # Define character sets for password generation
        lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
        uppercase_letters = lowercase_letters.upper()
        numbers = '1234567890'
        special_chars = '!@#$%^&*()'
        
        # Initialize empty password string
        random_password = ""

        # Generate 12-character password with random character selection
        while len(random_password) < 12:
            # Randomly choose a character set
            char_set = r.choice([lowercase_letters, uppercase_letters, numbers, special_chars])
            # Randomly choose a character from the selected set
            selected_char = r.choice(char_set)
            random_password += selected_char

        # Clear current password field and insert new password
        self.pass_entry.delete(0, END)  # Use END instead of len for complete clearing
        self.pass_entry.insert(0, random_password)
        # Validate the generated password immediately
        self.check_pass(random_password)
        # Debug output to console
        print(random_password)

    def check_email(self, email: str):
        """
        Validate email format using regex pattern.
        Updates UI with visual feedback.
        
        Args:
            email (str): Email address to validate
        """
        # Standard email regex pattern validation
        if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email):
            # Valid email - show green feedback
            self.email_entry.config(highlightbackground='green', highlightcolor='green', highlightthickness=2)
            self.email_valid_info.config(text='Valid email', fg='green')
            self.email_good = True
        else:
            # Invalid email - show red feedback
            self.email_entry.config(highlightbackground='red', highlightcolor='red', highlightthickness=2)
            self.email_valid_info.config(text='Invalid email', fg='red')
            self.email_good = False
            
    def check_pass(self, passwd):
        """
        Validate password strength (minimum 12 characters, allowed character set).
        
        Args:
            passwd (str): Password to validate
        """
        # Check for minimum length and allowed characters
        if re.match(r'[A-Za-z0-9!@#$%^&*()]{12,}', passwd):
            # Valid password - show green feedback
            self.pass_entry.config(highlightbackground='green', highlightcolor='green', highlightthickness=2)
            self.pass_valid_info.config(text='Valid password', fg='green')
            self.pass_good = True
        else:
            # Invalid password - show red feedback
            self.pass_entry.config(highlightbackground='red', highlightcolor='red', highlightthickness=2)
            self.pass_valid_info.config(text='Invalid password (min 12 chars)', fg='red')
            self.pass_good = False

    def check_url(self, url):
        """
        Validate website URL format (checks if field is not empty).
        Simple validation - just ensures user has entered something.
        
        Args:
            url (str): URL to validate
        """
        # Simple validation - just check if something is entered
        if url != "":
            self.url_good = True
        else:
            self.url_good = False
        
    def run_prog(self):
        """Start the main application loop."""
        self.window.mainloop()

# Application entry point
if __name__ == "__main__":
    app = PassWordGen()
    app.run_prog()