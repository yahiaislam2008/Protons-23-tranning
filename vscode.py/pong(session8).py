import turtle

import random

window = turtle.Screen()
window.title("Pong")
window.setup(width=800, height=600)
window.tracer(0)  # set delay for update drawings
window.bgcolor(.1, .1, .1)

ball = turtle.Turtle()
ball.speed(0)  
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(5,5)
color=("purple","pink","skyblue","yellow","orange","gray")


ball_dx = 1
ball_dy = 1

ball_speed = 2

line=turtle.Turtle()
line.goto(0,0)

line.shape("square")
line.color("white")
line.shapesize(stretch_len=0.1 ,stretch_wid=30)


player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.penup()
player1.goto(-350,0)
player1.color("red")


player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.penup()
player2.goto(350,0)
player2.color("blue")
p1_score = 0
p2_score = 0
pen=turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player1:0  player2:0",align="center",font=("Arial",24,"normal"))

def player1up():
    y=player1.ycor()
    y +=90
    player1.sety(y)

def player1down():
    y=player1.ycor()
    y -=90
    player1.sety(y)

def player2up():
    y=player2.ycor()
    y +=90
    player2.sety(y)

def player2down():
    y=player2.ycor()
    y -=90
    player2.sety(y)

window.listen()
window.onkey(player1up,"w")
window.onkey(player1down,"s")
window.onkey(player2up,"Up")
window.onkey(player2down,"Down")
players_speed = 20

ball_dx = random.randint(-100, 100)/100
ball_dy = random.randint(-100, 100)/100

def collisions(ball, ball_dx, ball_dy):
 
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1


   
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (player2.ycor()-60) and ball.ycor() < (player2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1
      

    return ball_dx, ball_dy

def detect_win(ball, ball_dx, ball_dy, p1_score, p2_score):
 
    r=random.choice(color)
    ball.setx(ball.xcor()+ball_dx)
    ball.sety(ball.ycor()+ball_dy)
    
    if ball.ycor()>290:
        ball.sety(290)
        ball_dy *=-1
        
        ball.color(r)

    if ball.ycor()<-290:
        ball.sety(-290)
        ball_dy *=-1

        ball.color(r)

    if ball.xcor()>390:
        ball.goto(0,0)
        ball_dx=ball_dx
        p1_score +=1
        pen.clear()
        pen.write("player1:{}      player2:{}".format(p1_score,p2_score),align="center",font=("Arial",24,"normal"))
    
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball_dx=ball_dx
        p2_score +=1
        pen.clear()
        pen.write("player1:{}      player2:{}".format(p1_score,p2_score),align="center",font=("Arial",24,"normal"))


    return ball_dx, ball_dy, p1_score, p2_score

while True:
    window.update()


    ball_dx, ball_dy = collisions(ball, ball_dx, ball_dy)
    ball_dx, ball_dy, p1_score, p2_score = detect_win(ball, ball_dx, ball_dy, p1_score, p2_score)



  