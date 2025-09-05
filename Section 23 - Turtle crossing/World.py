"""
World Module - Turtle Crossing Game

This module defines the World class which serves as the main game controller
and coordinator. It manages the game screen, UI elements, game loop, scoring,
level progression, and game over conditions.

Classes:
    World: Main game controller that orchestrates all game components
"""

from Player import Player
from Car import Car
import turtle as t
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from turtle import _Screen

class World():
    """
    World class that serves as the main game controller.
    
    This class coordinates all game components and manages:
    - Game screen setup and configuration
    - UI elements (score display, game over message)
    - Game state (spawning, scoring, level progression)
    - Main game loop timing and flow
    - Input handling and key bindings
    
    The World class follows the composition pattern, containing instances
    of Player and Car classes rather than inheriting from them.
    
    Attributes:
        screen (turtle.Screen): Main game screen
        score (int): Current player score (levels completed)
        scoring_turt (turtle.Turtle): Turtle object for displaying score
        game_over_turt (turtle.Turtle): Turtle object for game over message
        player (Player): The player-controlled turtle
        car (Car): The car manager handling all obstacles
        spawn_car (bool): Flag controlling when to spawn new cars
        defeat (bool): Flag indicating if game is over
    """
    
    def __init__(self):
        """
        Initialize the game world and all its components.
        
        Sets up:
        - Game screen with appropriate size and background
        - UI elements for score and game over display
        - Player and car objects
        - Input key bindings
        - Initial game state flags
        """
        # Screen setup and configuration
        self.screen = t.Screen()
        self.screen.setup(width=600, height=600)  # Set window size
        self.screen.bgcolor('white')              # White background
        self.screen.tracer(0)                     # Turn off animation for manual updates
        
        # Score tracking and display
        self.score = 0
        self.scoring_turt = t.Turtle()
        self.scoring_turt.hideturtle()            # Hide turtle, only show text
        self.scoring_turt.teleport(x=-290, y=275) # Position in top-left corner
        self.scoring_turt.write(
            f'Score: {self.score}', 
            align='left', 
            font=("Arial", 15, 'normal')
        )
        
        # Game over message display
        self.game_over_turt = t.Turtle()
        self.game_over_turt.hideturtle()          # Hide turtle, only show text
        self.game_over_turt.teleport(x=0)         # Center position for game over message
        
        # Initialize game objects
        self.player = Player(screen=self.screen)  # Player-controlled turtle
        self.car = Car(player=self.player)        # Car manager with player reference
        
        # Input handling - bind arrow keys to player movement methods
        self.screen.onkeypress(self.player.move_up, 'Up')
        self.screen.onkeypress(self.player.move_down, 'Down')
        self.screen.onkeypress(self.player.move_left, 'Left')
        self.screen.onkeypress(self.player.move_right, 'Right')
        self.screen.listen()                      # Enable keyboard input detection
        
        # Game state flags
        self.spawn_car = False                    # Controls when to spawn cars
        self.defeat = False                       # Tracks if game is over

    def game_loop(self):
        """
        Main game loop that runs continuously during gameplay.
        
        This method handles the core game logic flow:
        1. Spawn cars if needed (start of level)
        2. Check for player-car collisions (game over condition)
        3. Move cars and handle car looping
        4. Check for level completion and score updates
        5. Update screen display
        6. Schedule next loop iteration
        
        The loop runs at approximately 10 FPS (100ms intervals) for smooth
        but not too fast gameplay.
        """
        # Spawn cars at the beginning of each level
        if not self.spawn_car:
            print('Spawned Cars')  # Debug output
            self.car.spawn_car()
            self.spawn_car = True
        
        # Check for collision - end game if collision detected
        if self.car.check_collision_with_player():
            self.game_over()
            return  # Exit loop to stop game
        
        # Update car positions and handle looping
        self.car.move_cars()   # Move all cars leftward
        self.car.loop_cars()   # Loop cars that have exited screen
        
        # Check for level completion and update score
        self.increment_score()
        
        # Update screen display and schedule next loop iteration
        self.screen.update()                           # Refresh screen with new positions
        self.screen.ontimer(self.game_loop, 17)        # Schedule next loop in ~17ms (60 FPS)

    def increment_score(self):
        """
        Handle level completion and score progression.
        
        This method is called every frame to check if the player has
        reached the top of the screen (level cleared). When a level
        is completed:
        1. Reset player to starting position
        2. Increment score
        3. Increase game difficulty (car speed and count)
        4. Reset car spawning for next level
        5. Update score display
        
        The difficulty scaling makes each subsequent level more challenging
        by adding faster cars and more obstacles.
        """
        if self.player.level_cleared():
            # Reset player position for next level
            self.player.teleport(y=-290)
            
            # Increment score (represents levels completed)
            self.score += 1
            
            # Increase difficulty for next level
            self.car.increment_car_speed()        # Cars move faster
            self.car.increment_number_of_cars()   # More cars
            
            # Reset spawning flag to trigger new car generation
            self.spawn_car = False
            
            # Debug output and UI update
            print(f"Level {self.score} completed!")  # Debug output
            self.scoring_turt.clear()                # Clear old score
            self.scoring_turt.write(
                f'Score: {self.score}', 
                align='left', 
                font=("Arial", 15, 'normal')
            )

    def game_over(self):
        """
        Handle game over condition.
        
        This method is called when a collision is detected between
        the player and any car. It displays a game over message
        in the center of the screen.
        
        The game loop stops after this method is called, effectively
        ending the game. The player can still exit by clicking on
        the screen (handled in main.py).
        """
        self.game_over_turt.write(
            'Game Over', 
            align='center', 
            font=("Arial", 15, 'normal')
        )