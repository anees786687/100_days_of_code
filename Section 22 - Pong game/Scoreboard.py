from turtle import Turtle,Screen
class Scoreboard(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.score = 0
        self.screen = Screen()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.setpos((x_pos,y_pos))
        self.write(f"{self.score}", True, align='center', font=("Arial", 28, 'normal', 'bold'))


       
    
    def update_score(self, score):
        self.hideturtle()
        self.clear()
        self.score+=1
        self.write(f"{self.score}", True, align='center', font=("Arial", 28, 'normal', 'bold'))

        self.setpos(( self.x_pos, self.y_pos))
    

    def game_over(self):
        
        self.setpos(0,0)
        self.write(f"Game Over!", True, align='center', font=('Arial',15,'normal'))

