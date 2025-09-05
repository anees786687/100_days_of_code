from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setpos((0,280))
        self.write(f"Score: {self.score}", True, align='center', font=('Arial',12,'normal'))


       
    
    def update_score(self):
        self.hideturtle()
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}", True, align='center', font=('Arial',12,'normal'))
        self.setpos((0,280))
    

    def game_over(self):
        
        self.setpos(0,0)
        self.write(f"Game Over!", True, align='center', font=('Arial',15,'normal'))

