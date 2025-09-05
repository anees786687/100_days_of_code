from tkinter import *
import os

class PomodoroTimer:
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
    
    def __init__(self):
        # Initialize state variables
        self.reset_pressed = False
        self.long_break_over = False
        self.check_count = 0
        self.state = 'work'
        self.timer_job = None
        
        # Setup UI
        self.setup_ui()
    
    def setup_ui(self):
        """Initialize and configure the user interface"""
        self.window = Tk()
        self.window.config(padx=100, pady=50, bg=self.YELLOW)
        self.window.title('Pomodoro Timer')
        
        # Configure grid weights for better layout
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        
        # Title label
        self.timer_label = Label(
            text='Timer', 
            font=(self.FONT_NAME, 32, 'normal'),
            fg=self.GREEN, 
            bg=self.YELLOW
        )
        self.timer_label.grid(row=0, column=1)
        
        # Canvas with tomato image
        self.canvas = Canvas(
            width=200, 
            height=224, 
            bg=self.YELLOW, 
            highlightthickness=0
        )
        
        # Load image with error handling
        try:
            image_path = os.path.join(os.path.dirname(__file__), 'tomato.png')
            self.tomato_img = PhotoImage(file=image_path)
            self.canvas.create_image(100, 112, image=self.tomato_img)
        except Exception as e:
            print(f"Could not load tomato.png: {e}")
            # Create a simple circle as fallback
            self.canvas.create_oval(50, 50, 150, 150, fill=self.RED, outline=self.GREEN, width=3)
        
        # Timer text on canvas
        self.timer_text = self.canvas.create_text(
            103, 130, 
            text=f'{self.WORK_MIN}:00', 
            fill='white', 
            font=(self.FONT_NAME, 30, "bold")
        )
        self.canvas.grid(row=1, column=1)
        
        # Control buttons
        self.start_button = Button(
            text='Start', 
            command=self.start_timer,
            font=(self.FONT_NAME, 12),
            highlightthickness=0
        )
        self.start_button.grid(row=2, column=0, pady=20)
        
        self.reset_button = Button(
            text='Reset', 
            command=self.reset_timer,
            font=(self.FONT_NAME, 12),
            highlightthickness=0
        )
        self.reset_button.grid(row=2, column=2, pady=20)
        
        # Check marks for completed sessions
        self.check_label = Label(
            text='', 
            fg=self.GREEN, 
            bg=self.YELLOW, 
            font=(self.FONT_NAME, 25, 'normal')
        )
        self.check_label.grid(row=3, column=1)
    
    def start_timer(self):
        """Start the timer with the appropriate duration based on current state"""
        if self.state == 'work':
            self.countdown(self.WORK_MIN * 60)
            self.timer_label.config(text="Work", fg=self.GREEN)
        elif self.state == 'short_break':
            self.countdown(self.SHORT_BREAK_MIN * 60)
            self.timer_label.config(text="Short Break", fg=self.PINK)
        elif self.state == 'long_break':
            self.countdown(self.LONG_BREAK_MIN * 60)
            self.timer_label.config(text="Long Break", fg=self.RED)
    
    def countdown(self, count):
        """Handle the countdown mechanism"""
        if self.reset_pressed:
            return
            
        minutes = count // 60
        seconds = count % 60
        
        # Format time display
        time_text = f'{minutes}:{seconds:02d}'
        self.canvas.itemconfig(self.timer_text, text=time_text)
        
        if count > 0:
            self.timer_job = self.window.after(1000, self.countdown, count - 1)
        else:
            self.timer_finished()
    
    def timer_finished(self):
        """Handle timer completion and state transitions"""
        if self.state == 'work':
            self.check_count += 1
            self.update_check_marks()
            
            if self.check_count % 4 == 0:
                self.state = 'long_break'
            else:
                self.state = 'short_break'
        else:
            # Break finished, go back to work
            if self.state == 'long_break':
                self.check_count = 0
                self.update_check_marks()
            self.state = 'work'
        
        self.start_timer()
    
    def update_check_marks(self):
        """Update the checkmark display"""
        marks = '✓' * (self.check_count % 4)
        self.check_label.config(text=marks)
    
    def reset_timer(self):
        """Reset the timer to initial state"""
        self.reset_pressed = True
        
        if self.timer_job:
            self.window.after_cancel(self.timer_job)
        
        # Reset all state variables
        self.state = 'work'
        self.check_count = 0
        self.long_break_over = False
        self.reset_pressed = False
        
        # Reset UI
        self.timer_label.config(text="Timer", fg=self.GREEN)
        self.canvas.itemconfig(self.timer_text, text=f'{self.WORK_MIN}:00')
        self.check_label.config(text="")
    
    def run(self):
        """Start the application"""
        self.window.mainloop()


# Create and run the application
if __name__ == "__main__":
    app = PomodoroTimer()
    app.run()
