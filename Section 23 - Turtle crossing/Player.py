"""
Player Module - Turtle Crossing Game

This module defines the Player class which represents the player-controlled turtle
in the crossing game. The player can move in four directions and has boundary
checking to prevent going off-screen.

Classes:
    Player: Inherits from turtle.Turtle, handles player movement and boundary detection
"""

import turtle as t

class Player(t.Turtle):
    """
    Player class representing the player-controlled turtle.
    
    The player starts at the bottom of the screen and must navigate upward
    while avoiding cars. The player can move in all four directions but
    is constrained by screen boundaries.
    
    Attributes:
        screen (turtle.Screen): Reference to the game screen for boundary calculations
    """
    
    def __init__(self, screen: t.Screen):
        """
        Initialize the Player turtle.
        
        Args:
            screen (turtle.Screen): The game screen object for boundary checking
        """
        super().__init__()
        self.screen = screen
        
        # Configure player appearance and starting position
        self.shape('turtle')        # Use turtle shape for the player
        self.setheading(90)         # Face upward (north)
        self.teleport(y=-290)       # Start at bottom of screen
        self.penup()                # Don't draw lines when moving

    def move_up(self):
        """
        Move the player turtle upward by 10 pixels.
        
        This is the primary movement direction for progressing through levels.
        No boundary checking needed as player can always move up to clear levels.
        """
        self.setheading(90)  # Face north
        self.fd(10)          # Move forward 10 pixels

    def move_down(self):
        """
        Move the player turtle downward by 10 pixels.
        
        Includes boundary checking to prevent moving below the bottom edge.
        If at boundary, movement is prevented by calling fd(0).
        """
        self.setheading(270)  # Face south
        
        if self.out_of_bound():
            self.fd(0)        # Don't move if at boundary
        else:
            self.fd(10)       # Move forward 10 pixels

    def move_right(self):
        """
        Move the player turtle rightward by 10 pixels.
        
        Includes boundary checking to prevent moving beyond the right edge.
        If at boundary, movement is prevented by calling fd(0).
        """
        self.setheading(0)    # Face east
        
        if self.out_of_bound():
            self.fd(0)        # Don't move if at boundary
        else:
            self.fd(10)       # Move forward 10 pixels
    
    def move_left(self):
        """
        Move the player turtle leftward by 10 pixels.
        
        Includes boundary checking to prevent moving beyond the left edge.
        If at boundary, movement is prevented by calling fd(0).
        """
        self.setheading(180)  # Face west

        if self.out_of_bound():
            self.fd(0)        # Don't move if at boundary
        else:
            self.fd(10)       # Move forward 10 pixels

    def level_cleared(self):
        """
        Check if the player has reached the top of the screen to clear the level.
        
        Returns:
            bool: True if player's y-coordinate is at or above the top boundary,
                  False otherwise
        """
        if self.ycor() >= self.screen.window_height() // 2:
            return True
        return False
    
    def out_of_bound(self):
        """
        Check if the player is at or beyond the screen boundaries.
        
        This method prevents the player from moving outside the visible game area.
        It checks both horizontal (x-axis) and vertical (y-axis) boundaries.
        
        Returns:
            bool: True if player is at/beyond any boundary, False if within bounds
        """
        # Check if below bottom boundary (-270) or beyond left/right boundaries (±270)
        if self.ycor() < -270.0 or abs(self.xcor()) > 270:
            return True
        return False
    