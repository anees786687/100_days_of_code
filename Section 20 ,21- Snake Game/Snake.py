from turtle import Turtle, Screen
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.snake_body = []
        self.snake_pos = {}
        self.SNAKE_BOX_LEN = 20
        self.snake_len = 3
        self.screen = Screen()
        self.orientation = 'e'  # Initial orientation: east
        self.tail_orient = 'e'
        self.snake_alive = True
        self.head = None
        self.tail = None
        self.last_turn_time = time.time()  # Track the last time the snake turned
        self.turn_cooldown = 0.2  # Cooldown time in seconds

    def snake_init(self):
        for i in range(1, self.snake_len + 1):
            snake_part = Turtle()
            snake_part.shape('square')
            snake_part.color('white')
            snake_part.penup()
            snake_part.setx(-i * self.SNAKE_BOX_LEN)
            self.snake_body.append(snake_part)
            self.snake_pos[snake_part.pos()] = snake_part

        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]

        

   
    def move_snake(self):
    # Define the screen boundaries based on the actual game area
        screen_width = self.screen.window_width() // 2
        screen_height = self.screen.window_height() // 2

        # Wall collision detection
        head_x = self.snake_body[0].xcor()
        head_y = self.snake_body[0].ycor()

        if (head_x >= screen_width and self.orientation == 'e') or \
        (head_x <= -screen_width and self.orientation == 'w') or \
        (head_y >= screen_height and self.orientation == 'n') or \
        (head_y <= -screen_height and self.orientation == 's'):
            self.snake_alive = False  # Snake collides with the wall

         # Tail collision detection
        for segment in self.snake_body[1:]:  # Skip the head (first segment)
            if self.snake_body[0].distance(segment) < 10:  # Check if head is too close to any body segment
                self.snake_alive = False  # Snake collides with its tail
                break

        # Move the snake's body segments
        for part in range(len(self.snake_body) - 1, 0, -1):
            if not self.snake_alive:
                break
            # Move each segment to the position of the segment in front of it
            prev_part_pos = self.snake_body[part - 1].pos()
            self.snake_body[part].goto(prev_part_pos)
        # Move the snake's head forward
        if self.snake_alive:
            self.snake_body[0].forward(20)

    def can_turn(self):
        """Check if enough time has passed since the last turn."""
        return time.time() - self.last_turn_time >= self.turn_cooldown

    def turn_left(self):
        if self.can_turn():
            if self.orientation == 'n' and self.orientation != 's':  # Prevent reversing direction
                self.snake_body[0].lt(90)
                self.orientation = 'w'
                self.last_turn_time = time.time()
            elif self.orientation == 's' and self.orientation != 'n':
                self.snake_body[0].rt(90)
                self.orientation = 'w'
                self.last_turn_time = time.time()

    def turn_right(self):
        if self.can_turn():
            if self.orientation == 'n' and self.orientation != 's':  # Prevent reversing direction
                self.snake_body[0].rt(90)
                self.orientation = 'e'
                self.last_turn_time = time.time()
            elif self.orientation == 's' and self.orientation != 'n':
                self.snake_body[0].lt(90)
                self.orientation = 'e'
                self.last_turn_time = time.time()

    def turn_down(self):
        if self.can_turn():
            if self.orientation == 'e' and self.orientation != 'n':  # Prevent reversing direction
                self.snake_body[0].rt(90)
                self.orientation = 's'
                self.last_turn_time = time.time()
            elif self.orientation == 'w' and self.orientation != 'n':
                self.snake_body[0].lt(90)
                self.orientation = 's'
                self.last_turn_time = time.time()

    def turn_up(self):
        if self.can_turn():
            if self.orientation == 'e' and self.orientation != 's':  # Prevent reversing direction
                self.snake_body[0].lt(90)
                self.orientation = 'n'
                self.last_turn_time = time.time()
            elif self.orientation == 'w' and self.orientation != 's':
                self.snake_body[0].rt(90)
                self.orientation = 'n'
                self.last_turn_time = time.time()

    def get_snake_pos(self):
        return self.snake_body[0].pos()

    def generate_part(self):
        snake_part = Turtle()
        snake_part.shape('square')
        snake_part.color('white')
        snake_part.penup()
        snake_part.setx(-self.snake_len * self.SNAKE_BOX_LEN)
        self.snake_body.append(snake_part)
        self.snake_pos[snake_part.pos()] = snake_part
        self.tail = self.snake_body[-1]

        print(f"{snake_part.pos()}")