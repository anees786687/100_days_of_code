import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white','white')
        self.penup()
        self.ht()
        self.goto(0,230)
        self.write(f'Score {self.score}',move=False, align='center',font=('Arial',11,'normal'))

    def incement_score(self):
        self.clear()
        self.score += 1
        self.color('white','white')
        self.penup()
        self.ht()
        self.goto(0,230)
        self.write(f'Score {self.score}',move=False, align='center',font=('Arial',11,'normal'))

    def game_over_message(self):
        self.clear()
        self.color('white','white')
        self.penup()
        self.ht()
        self.goto(0,230)
        self.write(f'Game Over! Score {self.score}',move=False, align='center',font=('Arial',11,'normal'))


