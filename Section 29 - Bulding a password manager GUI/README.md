# 🔒 Password Manager GUI

A secure and user-friendly password manager built with Python's Tkinter library. This application provides real-time validation, automatic password generation, secure local storage, and search functionality for your credentials.

![Password Manager Screenshot](logo.png)

## ✨ Features

- **Real-time Input Validation**: Instant feedback with color-coded borders and messages
- **Secure Password Generation**: Create strong 12-character passwords with mixed character types
- **Data Persistence**: Save credentials to a local JSON file
- **Search Functionality**: Quickly find existing website credentials
- **User-friendly Interface**: Clean, intuitive GUI with visual feedback
- **Input Sanitization**: Automatic trimming of whitespace from inputs
- **Optional Username Field**: Flexibility for sites that use usernames instead of emails
- **Error Handling**: Robust file operations with proper exception handling

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually comes with Python installation)

### Installation

1. Clone or download this repository
2. Ensure you have a `logo.png` file in the same directory (optional)
3. Run the application:

```bash
python main.py
```

## 📖 How to Use

### Adding a New Password Entry

1. **Website**: Enter the website name (any format accepted)
2. **Email**: Enter your email address (validated in real-time)
3. **Username**: (Optional) Enter username if the site uses usernames
4. **Password**: Enter password manually or click "Generate Password"
5. **Save**: Click "Add" to save the entry

### Searching for Existing Entries

1. Enter the website name in the **Website** field
2. Click the **Search** button
3. If found, credentials will be displayed in a popup

### Password Generation

1. Click the **"Generate Password"** button
2. A secure 12-character password will be automatically created
3. The password includes uppercase, lowercase, numbers, and special characters

## 🔧 Technical Details

### Validation Rules

- **Email**: Must follow standard email format (user@domain.extension)
- **Password**: Minimum 12 characters, allows letters, numbers, and special characters
- **Website**: Any non-empty string is accepted

### File Format

Data is stored in `passwords.json` with the following structure:

```json
{
  "website_name": {
    "email": "user@example.com",
    "password": "secure_password_123",
    "username": "optional_username"
  }
}
```

### Real-time Validation

- **Green borders/text**: Valid input
- **Red borders/text**: Invalid input
- Validation occurs as you type (on `KeyRelease` events)

## 🔐 Security Considerations

⚠️ **IMPORTANT SECURITY NOTES:**

- This is a **learning project** and should NOT be used for real password management
- Passwords are stored in **plain text** JSON format
- No encryption or master password protection
- For real use, consider established password managers like:
  - Bitwarden
  - 1Password
  - LastPass
  - KeePass

## 🛠️ Code Structure

### Classes and Methods

- **`PassWordGen`**: Main application class
  - `init_ui()`: Creates the GUI interface
  - `search_details()`: Searches for existing website entries
  - `get_deets()`: Collects and saves user input
  - `gen_pass()`: Generates secure random passwords
  - `check_email()`: Validates email format
  - `check_pass()`: Validates password strength
  - `check_url()`: Validates website input

### Key Features

- **Event-driven validation**: Uses Tkinter event binding for real-time feedback
- **Exception handling**: Proper error handling for file operations
- **Modular design**: Separate methods for different functionalities
- **User feedback**: Visual and text feedback for all operations

## 🎯 Learning Objectives

This project demonstrates:

- **GUI Development**: Using Tkinter for desktop applications
- **Input Validation**: Real-time form validation with regex
- **File I/O**: Reading and writing JSON data
- **Error Handling**: Try/except blocks for robust operation
- **Event Handling**: Binding events to functions
- **Object-Oriented Programming**: Class-based application structure

## 🚀 Future Enhancements

Potential improvements could include:

- [ ] **Encryption**: Add password encryption for security
- [ ] **Master Password**: Implement master password protection
- [ ] **Import/Export**: Add CSV import/export functionality
- [ ] **Password Strength Meter**: Visual password strength indicator
- [ ] **Backup Features**: Automatic backup of password database
- [ ] **Dark Mode**: Theme switching capability
- [ ] **Password History**: Track password changes over time
- [ ] **Two-Factor Authentication**: TOTP code generation

## 🤝 Contributing

This is a learning project from the "100 Days of Code" course. Feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## 📝 License

This project is for educational purposes. Use responsibly and consider security implications before any real-world usage.

## 👨‍💻 Author

**Anees Alwani**  
*Date: September 5th, 2025*  
*Project: 100 Days of Code - Section 29*

---

⭐ **If you found this project helpful, please give it a star!**