# Turtle Crossing Game

A Frogger-style arcade game built with Python's Turtle module where the player must navigate a turtle across a busy road while avoiding moving cars.

## 🎮 Game Description

The player controls a turtle that must cross from the bottom of the screen to the top while avoiding randomly colored cars moving from right to left. Each successful crossing increases the player's score and makes the game progressively more difficult.

## 🕹️ How to Play

### Controls
- **Arrow Keys**: Move the turtle in four directions
  - ⬆️ **Up Arrow**: Move up (primary direction for progression)
  - ⬇️ **Down Arrow**: Move down
  - ⬅️ **Left Arrow**: Move left
  - ➡️ **Right Arrow**: Move right

### Objective
- Navigate the turtle from the bottom to the top of the screen
- Avoid colliding with any of the moving cars
- Each successful crossing increases your score by 1
- Try to achieve the highest score possible!

### Game Over
- The game ends when the turtle collides with any car
- Click anywhere on the screen to exit after game over

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system
- No additional packages required (uses built-in turtle module)

### Installation
1. Clone this repository or download the files
2. Ensure all Python files are in the same directory:
   - `main.py`
   - `Player.py`
   - `Car.py`
   - `World.py`

### Running the Game
```bash
python main.py
```

## 🎯 Game Features

### Progressive Difficulty
- **Car Speed**: Increases with each level completed
- **Car Count**: More cars spawn at higher levels
- **Collision Detection**: Precise distance-based collision system

### Smart Car Spawning
- Cars spawn at random positions with collision avoidance
- No two cars spawn too close to each other
- Robust algorithm prevents infinite loops while ensuring fair gameplay

### Continuous Gameplay
- Cars loop seamlessly from right to left
- Smooth animation at 10 FPS for optimal gameplay
- Real-time score display

## 📁 Project Structure

```
turtle-crossing/
├── main.py          # Main entry point and game initialization
├── Player.py        # Player turtle class with movement and boundary detection
├── Car.py          # Car management system with spawning and collision detection
├── World.py        # Game controller managing screen, UI, and game loop
└── README.md       # This file
```

### Module Descriptions

#### `main.py`
- Entry point of the application
- Initializes the game world
- Starts the main game loop
- Handles program exit

#### `Player.py`
- Defines the `Player` class inheriting from `turtle.Turtle`
- Handles player movement in four directions
- Implements boundary checking to prevent off-screen movement
- Detects level completion when reaching the top

#### `Car.py`
- Defines the `Car` class managing all obstacle cars
- Implements smart car spawning with overlap prevention
- Handles car movement and screen looping
- Provides collision detection with the player
- Manages difficulty scaling (speed and quantity)

#### `World.py`
- Main game controller and coordinator
- Sets up the game screen and UI elements
- Manages the game loop and timing
- Handles input key bindings
- Controls game state (scoring, level progression, game over)

## 🎨 Game Mechanics

### Collision Detection
- Uses distance-based collision detection
- Collision threshold: 19 pixels
- Immediate game over upon collision

### Level Progression
- Player must reach y-coordinate ≥ screen height/2 to complete level
- Automatic reset to starting position after level completion
- Score increments by 1 per completed level

### Difficulty Scaling
- **Car Speed**: +1 pixel per frame each level
- **Car Quantity**: +3 cars each level
- Cars maintain random colors and positions

## 🔧 Customization

You can easily modify the game by adjusting these parameters:

### In `Car.py`:
- `self.car_speed = 5` - Initial car speed
- `self.number_of_cars = 10` - Initial number of cars
- `min_distance = 30` - Minimum distance between cars
- `dist <= 19` - Collision detection threshold

### In `World.py`:
- `self.screen.setup(width=600, height=600)` - Screen size
- `self.screen.ontimer(self.game_loop, 100)` - Game speed (lower = faster)

### In `Player.py`:
- `self.fd(10)` - Player movement distance per key press
- Boundary values in `out_of_bound()` method

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements such as:
- Additional sound effects
- Enhanced graphics
- Power-ups or special abilities
- High score tracking
- Different difficulty modes

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎓 Educational Value

This project demonstrates several important programming concepts:
- **Object-Oriented Programming**: Classes, inheritance, composition
- **Game Development**: Game loops, collision detection, state management
- **Python Turtle Graphics**: 2D graphics, animation, event handling
- **Algorithm Design**: Collision avoidance, boundary checking, looping logic

Perfect for learning Python game development and understanding fundamental programming patterns!
