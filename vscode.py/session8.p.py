import turtle

sc=turtle.Screen()

mt=turtle.Turtle()
color=["red","blue","green","yellow","purple","pink","black","brown","cyan","baby blue","mint","maroon","gold","silver","orange"]
import random
def r():
    mt.setheading(0)
    c=random.choice(color)    
    mt.color(c)
    mt.shape("turtle")
def d():
    mt.setheading(270)
    c=random.choice(color)    
    mt.color(c)

    mt.shape("turtle")

    
def u():
    mt.setheading(90)
    c=random.choice(color)    
    mt.color(c)
    mt.shape("turtle")
def l():
    mt.setheading(180)
    c=random.choice(color)    
    mt.color(c)
    mt.shape("turtle")
    
    
    
turtle.listen()
turtle.onkey(r,"Right")
turtle.onkey(l,"Left")
turtle.onkey(u,"Up")
turtle.onkey(d,"Down")
mt.shapesize(7)
while True:


    mt.forward(5)