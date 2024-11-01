from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()




#checklist
#create the screen
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title('pong')


#Create and move a paddle; this will be the player paddle
paddle1 = Paddle((350, 0))
paddle2=Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(paddle1.go_up, "Up")
screen.onkeypress(paddle1.go_down, "Down")
screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle2.go_down, "s")
score = Scoreboard()


# Detect collission with wall and bounce

#Detect collision with paddle
#Detect when Paddle misses
#keep score

game_is_on = True
while game_is_on:
    time.sleep(ball.ballspeed)
    screen.update()
    ball.move()
    
    #Detect Collission
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce()
    
    #Collission with paddles
    if ball.distance(paddle1) < 50 and ball.xcor() > 320:
        ball.pbounce()
    
    if ball.distance(paddle2) < 50 and ball.xcor() > -320:
        ball.pbounce()
        
    if ball.xcor() > 380: 
        ball.reset_position()
        score.paddle2_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        score.paddle1_point()
        
        

        

screen.exitonclick()