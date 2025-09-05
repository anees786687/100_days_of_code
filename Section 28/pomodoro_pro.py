"""
Advanced Pomodoro Timer with professional coding standards
Demonstrates: Type hints, logging, error handling, separation of concerns,
documentation, testing support, and extensibility
"""

import logging
import os
from typing import Callable, Optional
from tkinter import Tk, Canvas, Label, Button, PhotoImage, messagebox

from config import PomodoroConfig
from models import TimerState, SessionData, UIElements


class PomodoroTimer:
    """
    A professional Pomodoro Timer application with advanced features.
    
    Features:
    - Configurable work/break durations
    - Visual and state management
    - Error handling and logging
    - Clean separation of concerns
    - Type hints and documentation
    """
    
    def __init__(self, config: Optional[PomodoroConfig] = None):
        """
        Initialize the Pomodoro Timer.
        
        Args:
            config: Configuration object, uses default if None
        """
        self.config = config or PomodoroConfig()
        self.session = SessionData()
        self.ui = UIElements()
        
        # Setup logging
        self._setup_logging()
        
        # Callbacks for extensibility
        self.on_work_complete: Optional[Callable] = None
        self.on_break_complete: Optional[Callable] = None
        self.on_session_reset: Optional[Callable] = None
        
        logger.info("Pomodoro Timer initialized")
    
    def _setup_logging(self):
        """Configure logging for the application"""
        global logger
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('pomodoro.log'),
                logging.StreamHandler()
            ]
        )
        logger = logging.getLogger(__name__)
    
    def setup_ui(self) -> None:
        """Initialize and configure the user interface"""
        try:
            self._create_main_window()
            self._create_title_label()
            self._create_timer_canvas()
            self._create_control_buttons()
            self._create_progress_display()
            
            logger.info("UI setup completed successfully")
            
        except Exception as e:
            logger.error(f"Failed to setup UI: {e}")
            messagebox.showerror("Error", f"Failed to initialize UI: {e}")
            raise
    
    def _create_main_window(self) -> None:
        """Create and configure the main window"""
        self.ui.window = Tk()
        self.ui.window.title('Pomodoro Timer Pro')
        self.ui.window.config(
            bg=self.config.COLORS['yellow'],
            **self.config.WINDOW_PADDING
        )
        
        # Configure grid weights for responsive layout
        for i in range(3):
            self.ui.window.columnconfigure(i, weight=1)
    
    def _create_title_label(self) -> None:
        """Create the title label"""
        self.ui.timer_label = Label(
            self.ui.window,
            text='Timer',
            font=self.config.FONTS['title'],
            fg=self.config.COLORS['green'],
            bg=self.config.COLORS['yellow']
        )
        self.ui.timer_label.grid(row=0, column=1, pady=(0, 20))
    
    def _create_timer_canvas(self) -> None:
        """Create the timer canvas with tomato image"""
        self.ui.canvas = Canvas(
            self.ui.window,
            bg=self.config.COLORS['yellow'],
            highlightthickness=0,
            **self.config.CANVAS_SIZE
        )
        
        # Load tomato image with fallback
        self._load_timer_background()
        
        # Create timer text
        initial_time = self._format_time(self.config.WORK_DURATION * 60)
        self.ui.timer_text = self.ui.canvas.create_text(
            100, 130,
            text=initial_time,
            fill='white',
            font=self.config.FONTS['timer']
        )
        
        self.ui.canvas.grid(row=1, column=1, pady=20)
    
    def _load_timer_background(self) -> None:
        """Load the tomato image or create a fallback"""
        try:
            image_path = os.path.join(os.path.dirname(__file__), 'tomato.png')
            if os.path.exists(image_path):
                self.tomato_img = PhotoImage(file=image_path)
                self.ui.canvas.create_image(100, 112, image=self.tomato_img)
                logger.info("Tomato image loaded successfully")
            else:
                raise FileNotFoundError("tomato.png not found")
                
        except Exception as e:
            logger.warning(f"Could not load tomato image: {e}. Using fallback.")
            # Create fallback design
            self.ui.canvas.create_oval(
                30, 30, 170, 170,
                fill=self.config.COLORS['red'],
                outline=self.config.COLORS['green'],
                width=3
            )
    
    def _create_control_buttons(self) -> None:
        """Create start and reset buttons"""
        self.ui.start_button = Button(
            self.ui.window,
            text='Start',
            command=self.start_timer,
            font=self.config.FONTS['button'],
            highlightthickness=0,
            bg=self.config.COLORS['green'],
            fg=self.config.COLORS['white'],
            padx=20
        )
        self.ui.start_button.grid(row=2, column=0, pady=20, sticky="ew", padx=(0, 10))
        
        self.ui.reset_button = Button(
            self.ui.window,
            text='Reset',
            command=self.reset_timer,
            font=self.config.FONTS['button'],
            highlightthickness=0,
            bg=self.config.COLORS['red'],
            fg=self.config.COLORS['white'],
            padx=20
        )
        self.ui.reset_button.grid(row=2, column=2, pady=20, sticky="ew", padx=(10, 0))
    
    def _create_progress_display(self) -> None:
        """Create the progress checkmarks display"""
        self.ui.check_label = Label(
            self.ui.window,
            text='',
            fg=self.config.COLORS['green'],
            bg=self.config.COLORS['yellow'],
            font=self.config.FONTS['checkmarks']
        )
        self.ui.check_label.grid(row=3, column=1, pady=10)
    
    def start_timer(self) -> None:
        """Start the timer based on current state"""
        if self.session.is_running:
            logger.warning("Timer is already running")
            return
        
        self.session.is_running = True
        self._update_ui_for_state()
        
        # Determine duration based on state
        duration_map = {
            TimerState.WORK: self.config.WORK_DURATION,
            TimerState.SHORT_BREAK: self.config.SHORT_BREAK_DURATION,
            TimerState.LONG_BREAK: self.config.LONG_BREAK_DURATION
        }
        
        duration_seconds = duration_map[self.session.current_state] * 60
        self.session.remaining_seconds = duration_seconds
        
        logger.info(f"Starting {self.session.current_state.value} timer for {duration_seconds//60} minutes")
        self._countdown()
    
    def _countdown(self) -> None:
        """Handle the countdown mechanism"""
        if not self.session.is_running:
            return
        
        # Update display
        time_text = self._format_time(self.session.remaining_seconds)
        self.ui.canvas.itemconfig(self.ui.timer_text, text=time_text)
        
        if self.session.remaining_seconds > 0:
            self.session.remaining_seconds -= 1
            self.session.timer_job_id = self.ui.window.after(1000, self._countdown)
        else:
            self._timer_completed()
    
    def _timer_completed(self) -> None:
        """Handle timer completion and state transitions"""
        self.session.is_running = False
        logger.info(f"{self.session.current_state.value} session completed")
        
        if self.session.current_state == TimerState.WORK:
            self.session.completed_sessions += 1
            self._update_progress_display()
            
            # Trigger callback
            if self.on_work_complete:
                self.on_work_complete()
            
            # Determine next state
            if self.session.completed_sessions % self.config.SESSIONS_BEFORE_LONG_BREAK == 0:
                self.session.current_state = TimerState.LONG_BREAK
            else:
                self.session.current_state = TimerState.SHORT_BREAK
        
        else:  # Break completed
            if self.on_break_complete:
                self.on_break_complete()
                
            # Reset progress after long break
            if self.session.current_state == TimerState.LONG_BREAK:
                self.session.completed_sessions = 0
                self._update_progress_display()
            
            self.session.current_state = TimerState.WORK
        
        # Auto-start next session
        self.start_timer()
    
    def _update_ui_for_state(self) -> None:
        """Update UI elements based on current state"""
        state_config = {
            TimerState.WORK: ("Work Time", self.config.COLORS['green']),
            TimerState.SHORT_BREAK: ("Short Break", self.config.COLORS['pink']),
            TimerState.LONG_BREAK: ("Long Break", self.config.COLORS['red'])
        }
        
        text, color = state_config[self.session.current_state]
        self.ui.timer_label.config(text=text, fg=color)
    
    def _update_progress_display(self) -> None:
        """Update the progress checkmarks"""
        active_sessions = self.session.completed_sessions % self.config.SESSIONS_BEFORE_LONG_BREAK
        checkmarks = '✓' * active_sessions
        self.ui.check_label.config(text=checkmarks)
    
    def reset_timer(self) -> None:
        """Reset the timer to initial state"""
        logger.info("Timer reset requested")
        
        # Cancel current timer
        if self.session.timer_job_id:
            self.ui.window.after_cancel(self.session.timer_job_id)
        
        # Reset session data
        self.session.reset()
        
        # Reset UI
        self.ui.timer_label.config(text="Timer", fg=self.config.COLORS['green'])
        initial_time = self._format_time(self.config.WORK_DURATION * 60)
        self.ui.canvas.itemconfig(self.ui.timer_text, text=initial_time)
        self.ui.check_label.config(text="")
        
        # Trigger callback
        if self.on_session_reset:
            self.on_session_reset()
        
        logger.info("Timer reset completed")
    
    def _format_time(self, seconds: int) -> str:
        """Format seconds into MM:SS format"""
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02d}"
    
    def get_session_stats(self) -> dict:
        """Get current session statistics"""
        return {
            'completed_sessions': self.session.completed_sessions,
            'current_state': self.session.current_state.value,
            'is_running': self.session.is_running,
            'remaining_time': self._format_time(self.session.remaining_seconds)
        }
    
    def run(self) -> None:
        """Start the application"""
        try:
            self.setup_ui()
            logger.info("Starting Pomodoro Timer application")
            self.ui.window.mainloop()
        except Exception as e:
            logger.error(f"Application error: {e}")
            raise
        finally:
            logger.info("Application shutting down")


def main():
    """Main function to run the application"""
    try:
        app = PomodoroTimer()
        
        # Example of adding callbacks for extensibility
        app.on_work_complete = lambda: print("🎉 Work session completed!")
        app.on_break_complete = lambda: print("☕ Break session completed!")
        
        app.run()
        
    except Exception as e:
        print(f"Failed to start application: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
