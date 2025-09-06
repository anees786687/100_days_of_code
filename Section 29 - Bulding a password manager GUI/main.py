"""
Password Manager GUI Application

A secure password manager with real-time validation and password generation.
Features:
- Real-time input validation for websites, emails, and passwords
- Automatic password generation
- Data persistence to text file
- User-friendly GUI with visual feedback

Author: Anees Alwani
Date: 5th September 2025
"""

from tkinter import *
from tkinter import messagebox # imorting message box, the first line doesnt implement modules but all the classes
import random as r
import os
import re  # For regex pattern matching

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

        self.init_ui()
    
    def init_ui(self):
        """Initialize and configure the user interface components."""
        # Configure main window
        self.window.config(padx=40, pady=40)
        self.window.title('Password Manager')

        # --- Logo Section ---
        self.img_frame = Frame(self.window)
        self.img_frame.grid(row=0, column=0, pady=(0, 20))
        self.canvas = Canvas(self.img_frame, width=200, height=190, highlightthickness=0)
        
        try:
            # Load and display logo image
            img_path = os.path.join(os.path.dirname(__file__), './logo.png')
            self.logo = PhotoImage(file=img_path)
            self.canvas.create_image(100, 95, image=self.logo)  # Centered positioning
        except Exception as e:
            print(f'Error while fetching image: {e}')
        
        self.canvas.grid(row=0, column=0)

        # --- Main Data Entry Frame ---
        self.data_frame = Frame(self.window)
        self.data_frame.grid(row=1, column=0, sticky='ew')

        # --- Website URL Input Section ---
        self.website_frame = Frame(self.data_frame)
        self.website_frame.grid(row=0, column=0, pady=5, sticky='ew')
        
        # Website label
        self.website_label = Label(self.website_frame, text='Website:', font=('Arial', 13), width=15, anchor='e')
        self.website_label.grid(row=0, column=0, padx=(0, 10), sticky='e')
        
        # Website entry field with styling
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
        
        # Validation feedback label
        self.website_valid_info = Label(self.website_frame, text="", fg="red", font=('Arial', 10))
        self.website_valid_info.grid(row=0, column=2, sticky='w')
        
        # --- Email Input Section ---
        self.email_frame = Frame(self.data_frame)
        self.email_frame.grid(row=1, column=0, pady=5, sticky='ew')
        
        self.email_label = Label(self.email_frame, text='Email:', font=('Arial', 13), width=15, anchor='e')
        self.email_label.grid(row=0, column=0, padx=(0, 10), sticky='e')
        
        self.email_entry = Entry(
            self.email_frame,
            width=30,
            font=('Arial', 10),
            highlightthickness=2,
            highlightcolor='blue'
        )
        self.email_entry.grid(row=0, column=1, sticky='w')
        
        # Real-time email validation
        self.email_entry.bind('<KeyRelease>', lambda event: self.check_email(self.email_entry.get()))
        
        self.email_valid_info = Label(self.email_frame, text="", fg="red", font=('Arial', 10))
        self.email_valid_info.grid(row=0, column=2, sticky='w')

        # --- Username Input Section (Optional) ---
        self.username_frame = Frame(self.data_frame)
        self.username_frame.grid(row=2, column=0, pady=5, sticky='ew')
        
        self.username_label = Label(self.username_frame, text='Username\n(if applicable):', font=('Arial', 13), width=15, anchor='e')
        self.username_label.grid(row=0, column=0, padx=(0, 10), sticky='e')
        
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
        
        self.pass_label = Label(self.pass_frame, text='Password:', font=('Arial', 13), width=15, anchor='e')
        self.pass_label.grid(row=0, column=0, padx=(0, 10), sticky='e')
        
        self.pass_entry = Entry(
            self.pass_frame,
            width=30,
            font=('Arial', 10),
            highlightthickness=2,
            highlightcolor='blue'
        )
        self.pass_entry.grid(row=0, column=1, sticky='w', padx=(0, 5))
        
        # Real-time password validation
        self.pass_entry.bind('<KeyRelease>', lambda event: self.check_pass(self.pass_entry.get()))
        
        self.pass_valid_info = Label(self.pass_frame, text="", fg="red", font=('Arial', 10))
        self.pass_valid_info.grid(row=1, column=1, sticky='ew')
        
        # Password generation button
        self.gen_pass_button = Button(self.pass_frame, text='Generate Password', width=15, command=self.gen_pass)
        self.gen_pass_button.grid(row=0, column=2, sticky='w')
        
        # --- Save Data Button ---
        self.add_button_frame = Frame(self.data_frame)
        self.add_button_frame.grid(row=4, column=0, pady=5, sticky='ew')
        
        self.add_button = Button(self.add_button_frame, text='Add', width=30, justify='center', command=self.get_deets)
        self.add_button.grid(row=0, column=1, columnspan=2, sticky='e', padx=(150, 0))
    
    def get_deets(self):
        """
        Collect and save user input data to file.
        Only saves if all required fields are valid.
        """
        # Get and clean input data
        self.website = self.website_entry.get().strip()
        self.username = self.username_entry.get().strip() if self.username_entry.get() != "" else None
        self.email = self.email_entry.get().strip()
        self.passwd = self.pass_entry.get().strip()

        # Only save if all validations pass
        if self.email_good and self.pass_good and self.url_good:
            # Creating a message box for success
            messagebox.showinfo(title="Success!", message='Details successfully stored')
            # Reset validation flags after successful save
            self.email_good = False
            self.pass_good = False
            self.url_good = False

            # Clearing the fields
            self.website_entry.delete(0, len(self.website))
            self.website_entry.config(highlightthickness=0)
            self.website_valid_info.config(text="")

            if self.username:
                self.username_entry.delete(0, len(self.username))
                self.username_entry.config(highlightthickness=0)
            
            self.email_entry.delete(0, len(self.email))
            self.email_entry.config(highlightthickness=0)
            self.email_valid_info.config(text="")

            self.pass_entry.delete(0, len(self.passwd))
            self.pass_entry.config(highlightthickness=0)
            self.pass_valid_info.config(text="")

            print(f'website: {self.website}, email: {self.email}, pass: {self.passwd}')
            
            # Save to file with proper formatting
            with open('passwords.txt', mode='a') as file:
                if self.username:
                    file.write(f'website:{self.website}|username:{self.username}|email:{self.email}|pass:{self.passwd}\n')
                else:
                    file.write(f'website:{self.website}|email:{self.email}|pass:{self.passwd}\n')

    def gen_pass(self):
        """
        Generate a secure random password with mixed character types.
        Automatically populates the password field.
        """
        # Character sets for password generation
        lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
        uppercase_letters = lowercase_letters.upper()
        numbers = '1234567890'
        special_chars = '!@#$%^&*()'
        
        random_password = ""

        # Generate 12-character password with random character selection
        while len(random_password) < 12:
            char_set = r.choice([lowercase_letters, uppercase_letters, numbers, special_chars])
            selected_char = r.choice(char_set)
            random_password += selected_char

        # Clear field and insert new password
        self.pass_entry.delete(0, len(random_password))
        self.pass_entry.insert(0, random_password)
        self.check_pass(random_password)
        print(random_password)

    def check_email(self, email: str):
        """
        Validate email format using regex pattern.
        Updates UI with visual feedback.
        
        Args:
            email (str): Email address to validate
        """
        # Standard email regex pattern
        if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email):
            # Valid email - green feedback
            self.email_entry.config(highlightbackground='green', highlightcolor='green', highlightthickness=2)
            self.email_valid_info.config(text='Valid email', fg='green')
            self.email_good = True
        else:
            # Invalid email - red feedback
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
            # Valid password - green feedback
            self.pass_entry.config(highlightbackground='green', highlightcolor='green', highlightthickness=2)
            self.pass_valid_info.config(text='Valid password', fg='green')
            self.pass_good = True
        else:
            # Invalid password - red feedback
            self.pass_entry.config(highlightbackground='red', highlightcolor='red', highlightthickness=2)
            self.pass_valid_info.config(text='Invalid password (min 12 chars)', fg='red')
            self.pass_good = False

    def check_url(self, url):
        """
        Validate website URL format (expects www.domain.extension format).
        
        Args:
            url (str): URL to validate
        """
        # Simple URL pattern validation
        if re.match(r'^www\.[A-Za-z0-9]+\.[a-zA-Z]+$', url):
            # Valid URL - green feedback
            self.website_entry.config(highlightbackground='green', highlightcolor='green', highlightthickness=2)
            self.website_valid_info.config(text='Valid website', fg='green')
            self.url_good = True
        else:
            # Invalid URL - red feedback
            self.website_entry.config(highlightbackground='red', highlightcolor='red', highlightthickness=2)
            self.website_valid_info.config(text='Invalid website', fg='red')
            self.url_good = False
        
    def run_prog(self):
        """Start the main application loop."""
        self.window.mainloop()

# Application entry point
if __name__ == "__main__":
    app = PassWordGen()
    app.run_prog()
