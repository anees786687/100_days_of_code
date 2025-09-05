# models.py - Data structures for better organization
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class TimerState(Enum):
    """Enum for different timer states"""
    WORK = "work"
    SHORT_BREAK = "short_break"
    LONG_BREAK = "long_break"
    STOPPED = "stopped"

@dataclass
class SessionData:
    """Data class to track session information"""
    current_state: TimerState = TimerState.WORK
    completed_sessions: int = 0
    is_running: bool = False
    remaining_seconds: int = 0
    timer_job_id: Optional[str] = None
    
    def reset(self):
        """Reset session data to initial state"""
        self.current_state = TimerState.WORK
        self.completed_sessions = 0
        self.is_running = False
        self.remaining_seconds = 0
        self.timer_job_id = None

@dataclass 
class UIElements:
    """Data class to hold UI element references"""
    window: Optional[object] = None
    canvas: Optional[object] = None
    timer_text: Optional[object] = None
    timer_label: Optional[object] = None
    check_label: Optional[object] = None
    start_button: Optional[object] = None
    reset_button: Optional[object] = None
