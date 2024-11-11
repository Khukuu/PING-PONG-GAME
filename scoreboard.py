from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.paddle1score = 0
        self.paddle2score = 0
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.paddle2score, align = 'center', font = ('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.paddle1score, align = 'center', font = ('Courier', 80, 'normal'))
        
    def paddle1_point(self):
        self.paddle1score += 1
        self.update_score()
        
    def paddle2_point(self):
        self.paddle2score += 1
        self.update_score()
    
        