# config.py - Separate configuration file
class PomodoroConfig:
    """Configuration settings for the Pomodoro Timer"""
    
    # Time settings (in minutes)
    WORK_DURATION = 25
    SHORT_BREAK_DURATION = 5
    LONG_BREAK_DURATION = 20
    SESSIONS_BEFORE_LONG_BREAK = 4
    
    # UI Colors
    COLORS = {
        'pink': "#e2979c",
        'red': "#e7305b", 
        'green': "#9bdeac",
        'yellow': "#f7f5dd",
        'white': "#ffffff"
    }
    
    # UI Settings
    WINDOW_PADDING = {'padx': 100, 'pady': 50}
    CANVAS_SIZE = {'width': 200, 'height': 224}
    FONTS = {
        'title': ("Courier", 32, 'normal'),
        'timer': ("Courier", 30, "bold"),
        'button': ("Courier", 12),
        'checkmarks': ("Courier", 25, 'normal')
    }
    
    # Audio settings (for future sound notifications)
    SOUNDS = {
        'work_complete': 'sounds/work_done.wav',
        'break_complete': 'sounds/break_done.wav'
    }
