"""
Car Module - Turtle Crossing Game

This        self.cars_initial_x = []        # Store initial positions for looping cars
        self.player = player            # Reference to player for collision detection
        self.car_speed = 1.5            # Initial car movement speed (pixels per frame) - adjusted for 60 FPS
        self.number_of_cars = 10        # Initial number of cars to spawnule defines the Car class which manages all the moving obstacles (cars)
in the crossing game. It handles car spawning with collision avoidance,
movement, looping, and collision detection with the player.

Classes:
    Car: Manages a collection of car turtles that move across the screen
"""

import turtle as t
import random as r
import math as m
from Player import Player

class Car():
    """
    Car class that manages all moving car obstacles in the game.
    
    This class handles:
    - Spawning cars at random positions without overlap
    - Moving all cars from right to left across the screen
    - Looping cars back to the right side when they exit left
    - Detecting collisions with the player
    - Scaling difficulty by increasing speed and number of cars
    
    Attributes:
        screen (turtle.Screen): Reference to the game screen
        cars (list): List of all car turtle objects
        cars_initial_x (list): List storing initial x-coordinates for car looping
        player (Player): Reference to the player object for collision detection
        car_speed (int): Speed at which cars move (pixels per frame)
        number_of_cars (int): Number of cars to spawn per level
    """
    
    def __init__(self, player: Player):
        """
        Initialize the Car manager.
        
        Args:
            player (Player): The player object for collision detection
        """
        super().__init__()
        self.screen = t.Screen()        # Get screen reference for boundary calculations
        self.cars = []                  # List to store all car turtle objects
        self.cars_initial_x = []        # Store initial positions for looping cars
        self.player = player            # Reference to player for collision detection
        self.car_speed = 1              # Initial car movement speed (pixels per frame) - adjusted for 60 FPS
        self.number_of_cars = 5        # Initial number of cars to spawn

    def spawn_car(self):
        """
        Spawn cars at random positions across the screen.
        
        This method creates the specified number of cars with random colors
        and positions them on the screen. It uses a robust algorithm to
        prevent cars from spawning too close to each other.
        
        Algorithm:
        1. For each car to spawn, generate random positions
        2. Check if position conflicts with existing cars
        3. If conflict, try again up to max_attempts times
        4. If no valid position found, place anyway to prevent infinite loops
        
        Each car is configured with:
        - Square shape stretched to look like a car (2x1 ratio)
        - Random RGB color
        - Pen up to prevent drawing lines
        """
        min_distance = 50       # Minimum distance between cars (pixels)
        max_attempts = 100      # Maximum attempts to find valid position
        
        for _ in range(0, self.number_of_cars):
            # Create new car turtle
            temp = t.Turtle()
            temp.shape('square')
            temp.shapesize(stretch_len=2.0, stretch_wid=1.0)  # Make it look like a car
            
            # Generate random color (RGB values 0-1)
            temp.color(
                r.uniform(0.0, 255.0)/255.0, 
                r.uniform(0.0, 255.0)/255.0, 
                r.uniform(0.0, 255.0)/255.0
            )
            temp.penup()
            
            # Find a valid position that doesn't overlap with existing cars
            valid_position_found = False
            attempts = 0
            
            while not valid_position_found and attempts < max_attempts:
                # Generate random position within screen bounds
                temp_x = r.choice(list(range(-300, 300, 10)))  # x: left to right side
                temp_y = r.choice(list(range(-250, 280, 10)))  # y: avoid player start area
                
                # Check if this position is far enough from all existing cars
                position_valid = True
                for car in self.cars:
                    car: t.Turtle
                    # Calculate Euclidean distance between proposed position and existing car
                    dist = m.sqrt((temp_x - car.xcor())**2 + (temp_y - car.ycor())**2)
                    if dist < min_distance:
                        position_valid = False
                        break
                
                if position_valid:
                    valid_position_found = True
                else:
                    attempts += 1
            
            # Fallback: if no valid position found after max attempts, place anyway
            # This prevents infinite loops while ensuring all cars are spawned
            if not valid_position_found:
                temp_x = r.choice(list(range(300, 600, 10)))   # Place on right side
                temp_y = r.choice(list(range(-270, 280, 10)))  # Random y position
            
            # Position the car and add to tracking lists
            temp.teleport(x=temp_x, y=temp_y)
            self.cars_initial_x.append(temp.xcor())  # Store for looping logic
            self.cars.append(temp)

    def move_cars(self):
        """
        Move all cars leftward by the current car speed.
        
        This method is called every frame to animate the cars moving
        from right to left across the screen, creating the obstacle
        challenge for the player.
        """
        for car in self.cars:
            car: t.Turtle
            car.setx(car.xcor() - self.car_speed)  # Move left by car_speed pixels

    def get_car_list(self) -> list:
        """
        Get the list of all car turtle objects.
        
        Returns:
            list: List containing all car turtle objects
        """
        return self.cars
    
    def loop_cars(self):
        """
        Loop cars back to the right side when they exit the left side of screen.
        
        This creates a continuous stream of cars by repositioning cars that
        have moved off the left edge back to the right edge, maintaining
        the constant challenge for the player.
        
        The looping position (x=320) is slightly off-screen to the right,
        creating a smooth appearance of new cars entering the screen.
        """
        for i, car in enumerate(self.cars):
            car: t.Turtle
            # Check if car has moved past the left edge of screen
            if car.xcor() < -self.screen.window_width() // 2 - 20:
                car.teleport(x=320)  # Move to right side, keep same y position

    def check_collision_with_player(self):
        """
        Check if any car has collided with the player.
        
        Uses distance-based collision detection. If any car is within
        19 pixels of the player, a collision is registered.
        
        Returns:
            bool: True if collision detected, False otherwise
        """
        for car in self.cars:
            car: t.Turtle
            # Calculate distance between car and player
            dist = car.distance(self.player.xcor(), self.player.ycor())
            if dist <= 15:  # Collision threshold - tuned for better gameplay balance
                return True
            
        return False
    
    def increment_car_speed(self):
        """
        Increase the speed of all cars by 0.2 pixels per frame.
        
        This method is called when the player clears a level,
        making the game progressively more difficult.
        Adjusted for 60 FPS gameplay.
        """
        self.car_speed += 0.2

    def increment_number_of_cars(self):
        """
        Increase the number of cars to spawn by 3.
        
        This method is called when the player clears a level,
        adding more obstacles to increase difficulty.
        Note: Cars are only spawned at level start, so this
        affects the next level's car count.
        """
        self.number_of_cars += 1
        for car in self.cars:
            car: t.Turtle
            car.hideturtle()
        self.cars.clear()