"""
Turtle Crossing Game - Main Entry Point

This is a Frogger-style game where the player (turtle) must cross a busy road
while avoiding moving cars. The goal is to reach the top of the screen to
advance to the next level.

Game Controls:
- Arrow Keys: Move the turtle up, down, left, right
- Click anywhere on screen to exit

Author: Anees Alwani
Date: 20-8-2025
"""
from World import World

# Initialize the game world which sets up the screen, player, cars, and game mechanics
world = World()

# Start the main game loop which handles:
# - Car movement and spawning
# - Collision detection
# - Score tracking
# - Level progression
world.game_loop()

# Set up exit condition - clicking anywhere on the screen will close the game
world.screen.exitonclick()