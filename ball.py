from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(0,0)
        self.xmove = 10
        self.ymove = 10
        self.ballspeed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.ymove *= -1
        
    def pbounce(self):
        self.xmove *= -1
        self.ballspeed *= 0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.pbounce()
        self.ballspeed = 0.1