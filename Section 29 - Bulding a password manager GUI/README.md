# 🔒 Password Manager GUI

A secure and user-friendly password manager built with Python's Tkinter library. This application provides real-time validation, automatic password generation, and secure local storage of your credentials.

![Password Manager Screenshot](logo.png)

## ✨ Features

- **Real-time Input Validation**: Instant feedback with color-coded borders and messages
- **Secure Password Generation**: Create strong 12-character passwords with mixed character types
- **Data Persistence**: Save credentials to a local text file
- **User-friendly Interface**: Clean, intuitive GUI with visual feedback
- **Input Sanitization**: Automatic trimming of whitespace from inputs
- **Optional Username Field**: Flexibility for sites that use usernames instead of emails

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

1. **Website**: Enter the website URL (format: www.example.com)
2. **Email**: Enter your email address
3. **Username**: (Optional) Enter username if the site uses usernames
4. **Password**: Enter your password or use the "Generate Password" button
5. **Add**: Click the "Add" button to save (only works when all required fields are valid)

### Real-time Validation

The application provides instant feedback as you type:

- ✅ **Green border/text**: Valid input
- ❌ **Red border/text**: Invalid input

#### Validation Rules

- **Website**: Must follow format `www.domain.extension`
- **Email**: Must be a valid email format (user@domain.extension)
- **Password**: Minimum 12 characters, containing letters, numbers, and special characters

### Password Generation

Click the "Generate Password" button to create a secure 12-character password that includes:
- Lowercase letters (a-z)
- Uppercase letters (A-Z)
- Numbers (0-9)
- Special characters (!@#$%^&*())

## 💾 Data Storage

Passwords are saved to `passwords.txt` in the following format:

```
website:www.example.com|email:user@email.com|pass:securepassword123
website:www.github.com|username:myusername|email:user@email.com|pass:anotherpassword456
```

## 🔧 Technical Details

### Architecture

The application follows an object-oriented design with a single `PassWordGen` class that handles:

- GUI initialization and layout
- Real-time input validation using regex patterns
- Event handling for user interactions
- File I/O operations for data persistence

### Key Technologies

- **Tkinter**: GUI framework
- **Regular Expressions**: Input validation
- **Event Binding**: Real-time validation using `<KeyRelease>` events
- **File I/O**: Local data storage

### Validation Patterns

```python
# Email validation
r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

# Website validation  
r'^www\.[A-Za-z0-9]+\.[a-zA-Z]+$'

# Password validation
r'[A-Za-z0-9!@#$%^&*()]{12,}'
```

## 📁 File Structure

```
password-manager/
│
├── main.py              # Main application file
├── logo.png            # Application logo (optional)
├── passwords.txt       # Generated password storage file
└── README.md           # This file
```

## 🛡️ Security Considerations

⚠️ **Important Security Notes:**

- Passwords are stored in **plain text** in `passwords.txt`
- This is a **learning project** and not suitable for production use
- For real password management, use established tools like:
  - Bitwarden
  - LastPass
  - 1Password
  - KeePass

## 🔮 Future Enhancements

Potential improvements for this project:

- [ ] **Encryption**: Encrypt stored passwords
- [ ] **Master Password**: Add authentication to access the app
- [ ] **Search Functionality**: Find stored passwords by website
- [ ] **Edit/Delete**: Modify or remove existing entries
- [ ] **Import/Export**: CSV or JSON file support
- [ ] **Password Strength Meter**: Visual indicator of password strength
- [ ] **Auto-fill**: Browser integration capabilities
- [ ] **Backup**: Cloud storage options

## 🐛 Known Issues

- Logo image loading may fail if `logo.png` is not present (handled gracefully)
- Website validation is strict and may not accept all valid URL formats
- No duplicate checking - same website can be added multiple times

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📚 Learning Objectives

This project demonstrates:

- GUI development with Tkinter
- Real-time input validation
- Event-driven programming
- File I/O operations
- Regular expressions
- Object-oriented programming
- Error handling

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created as part of the "100 Days of Code" course on Udemy.

---

**⚡ Quick Start Command:**
```bash
python main.py
```

**🎯 Remember:** This is a learning project. For real password management, use established, security-audited tools!
