import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.color('white','white')
        self.penup()
        self.ht()
        self.goto(0,230)
        self.write(f'Score {self.score} | High score: {self.high_score}',move=False, align='center',font=('Arial',11,'normal'))

    def incement_score(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_high_score()
        self.color('white','white')
        self.penup()
        self.ht()
        self.goto(0,230)
        self.write(f'Score {self.score} | High Score: {self.high_score}',move=False, align='center',font=('Arial',11,'normal'))

    def game_over_message(self):
        self.clear()
        self.color('white','white')
        self.penup()
        self.ht()
        self.goto(0,230)
        self.write(f'Game Over! Score {self.score}',move=False, align='center',font=('Arial',11,'normal'))

    def write_score_after_reset(self):
        self.clear()
        self.score = 0
        
        self.write(f'Score {self.score} | High Score: {self.high_score}',move=False, align='center',font=('Arial',11,'normal'))

    def store_high_score(self):
        with open('high_score.txt', mode='w') as file:
            file.write(f"{self.high_score}")
