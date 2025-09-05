"""
Unit tests for the Pomodoro Timer
Demonstrates: Test-driven development, mocking, edge case handling
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add the parent directory to the path to import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models import TimerState, SessionData
from config import PomodoroConfig


class TestSessionData(unittest.TestCase):
    """Test cases for SessionData class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.session = SessionData()
    
    def test_initial_state(self):
        """Test initial session state"""
        self.assertEqual(self.session.current_state, TimerState.WORK)
        self.assertEqual(self.session.completed_sessions, 0)
        self.assertFalse(self.session.is_running)
        self.assertEqual(self.session.remaining_seconds, 0)
    
    def test_reset(self):
        """Test session reset functionality"""
        # Modify session state
        self.session.current_state = TimerState.SHORT_BREAK
        self.session.completed_sessions = 3
        self.session.is_running = True
        self.session.remaining_seconds = 120
        
        # Reset and verify
        self.session.reset()
        self.assertEqual(self.session.current_state, TimerState.WORK)
        self.assertEqual(self.session.completed_sessions, 0)
        self.assertFalse(self.session.is_running)
        self.assertEqual(self.session.remaining_seconds, 0)


class TestPomodoroConfig(unittest.TestCase):
    """Test cases for PomodoroConfig class"""
    
    def test_default_values(self):
        """Test default configuration values"""
        config = PomodoroConfig()
        self.assertEqual(config.WORK_DURATION, 25)
        self.assertEqual(config.SHORT_BREAK_DURATION, 5)
        self.assertEqual(config.LONG_BREAK_DURATION, 20)
        self.assertEqual(config.SESSIONS_BEFORE_LONG_BREAK, 4)
    
    def test_colors_exist(self):
        """Test that all required colors are defined"""
        config = PomodoroConfig()
        required_colors = ['pink', 'red', 'green', 'yellow', 'white']
        for color in required_colors:
            self.assertIn(color, config.COLORS)


class TestPomodoroTimerLogic(unittest.TestCase):
    """Test cases for PomodoroTimer business logic"""
    
    def setUp(self):
        """Set up test fixtures"""
        # We'll mock the UI components since we're testing logic only
        with patch('pomodoro_pro.Tk'), \
             patch('pomodoro_pro.Canvas'), \
             patch('pomodoro_pro.Label'), \
             patch('pomodoro_pro.Button'):
            
            from pomodoro_pro import PomodoroTimer
            self.timer = PomodoroTimer()
            self.timer.ui.window = Mock()
            self.timer.ui.canvas = Mock()
            self.timer.ui.timer_text = Mock()
    
    def test_format_time(self):
        """Test time formatting function"""
        self.assertEqual(self.timer._format_time(0), "0:00")
        self.assertEqual(self.timer._format_time(60), "1:00")
        self.assertEqual(self.timer._format_time(125), "2:05")
        self.assertEqual(self.timer._format_time(3661), "61:01")
    
    def test_session_stats(self):
        """Test session statistics"""
        stats = self.timer.get_session_stats()
        expected_keys = ['completed_sessions', 'current_state', 'is_running', 'remaining_time']
        
        for key in expected_keys:
            self.assertIn(key, stats)
        
        self.assertEqual(stats['current_state'], 'work')
        self.assertFalse(stats['is_running'])


class TestTimerStateTransitions(unittest.TestCase):
    """Test state transition logic"""
    
    def setUp(self):
        """Set up test fixtures"""
        with patch('pomodoro_pro.Tk'), \
             patch('pomodoro_pro.Canvas'), \
             patch('pomodoro_pro.Label'), \
             patch('pomodoro_pro.Button'):
            
            from pomodoro_pro import PomodoroTimer
            self.timer = PomodoroTimer()
            self.timer.ui.window = Mock()
            self.timer.ui.canvas = Mock()
            self.timer.ui.timer_text = Mock()
            self.timer.ui.timer_label = Mock()
            self.timer.ui.check_label = Mock()
    
    def test_work_to_short_break_transition(self):
        """Test transition from work to short break"""
        self.timer.session.current_state = TimerState.WORK
        self.timer.session.completed_sessions = 1
        
        # Simulate timer completion
        self.timer._timer_completed()
        
        self.assertEqual(self.timer.session.current_state, TimerState.SHORT_BREAK)
        self.assertEqual(self.timer.session.completed_sessions, 2)
    
    def test_work_to_long_break_transition(self):
        """Test transition from work to long break after 4 sessions"""
        self.timer.session.current_state = TimerState.WORK
        self.timer.session.completed_sessions = 3  # This will be the 4th session
        
        # Simulate timer completion
        self.timer._timer_completed()
        
        self.assertEqual(self.timer.session.current_state, TimerState.LONG_BREAK)
        self.assertEqual(self.timer.session.completed_sessions, 4)


if __name__ == '__main__':
    # Create a test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestSessionData,
        TestPomodoroConfig,
        TestPomodoroTimerLogic,
        TestTimerStateTransitions
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Exit with appropriate code
    sys.exit(0 if result.wasSuccessful() else 1)
