import turtle
import random
import time
windoes=turtle.Screen()
windoes.title("Snake game")
windoes.bgcolor("blue")
windoes.setup(width=600,height=600)
windoes.tracer(0)
delay=0.1
high_score=0
score=0
head=turtle.Turtle()
head.penup()
head.shape("square")
head.color("white")
head.goto(0,0)

head.direction="Stop"

food=turtle.Turtle()
food.penup()
food.speed(0)
food.shape("circle")
food.color("green")
food.goto(100,100)

pen=turtle.Turtle()
pen.penup()
pen.color("yellow")
pen.speed(0)
pen.goto(0,260)
pen.hideturtle()
pen.write("Score:0  High score:0",align="center",font=("courier","24","bold"))



def go_up():
    if head.direction!="Down":
        head.direction="Up"
        y=head.ycor()
        y+=20
        head.sety(y)
        
def go_down():        
    if head.direction!="Up":
        head.direction= "Down" 
        y=head.ycor()
        y-=20
        head.sety(y)

def go_right() :       
    if head.direction!="Left":
        head.direction="Right"
        x=head.xcor()
        x+=20
        head.setx(x)

def go_left():
    if head.direction!="Right":
        head.direction="Left"
        x=head.xcor()
        x-=20
        head.setx(x)

windoes.listen() 
windoes.onkeypress(go_up,"Up")
windoes.onkeypress(go_down,"Down")  
windoes.onkeypress(go_right,"Right") 
windoes.onkeypress(go_left,"Left") 

body_parts=[]

while True:
    windoes.update()
    if head.ycor()>290  or head.ycor()<-290  or head.xcor()>290  or head.xcor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="Stop"
        colors=(["red","orange","purple"])
        food.color(random.choice(colors))
        for part in body_parts:
            part.goto(1000,1000)
            #part.hideturtle()
        body_parts.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score:{}  High score:{}".format(score,high_score),align="center",font=("courier","24","bold"))

    if head.distance(food)<20:
        x=random.randrange(-270,270)
        y=random.randrange(-270,270)
        food.goto(x,y)
        colors=["red","green","purple"]
        food.color(random.choice(colors))
        #food.showturtle()
        new_part=turtle.Turtle()
        new_part.shape("square")
        new_part.color("orange")
        new_part.speed(0)
        new_part.penup()
        body_parts.append(new_part)
        delay -=0.001
        score+=10
        

    if score> high_score:
        high_score=score
    pen.clear()
    pen.write("Score:{}   High score:{}".format(score,high_score),align="center",font=("courier",24,"bold"))


        
 #   for i in range(len(body_parts)):
  #          if i==0:
   #           body_parts[0].goto(head.xcor(),head.ycor())
    #        else:
     #           body_parts[i].goto(body_parts[i-1].xcor(),body_parts[i-1].ycor())

    for index in range(len(body_parts)-1,0,-1):
        x=body_parts[index-1].xcor()
        y=body_parts[index-1].ycor()
        body_parts[index].goto(x,y)
    if len(body_parts)>0:
        x=head.xcor()
        y=head.ycor()
        body_parts[0].goto(x,y)
    #move()


    for part in body_parts:
        if part.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="Stop"
            colors=["red","orange","purple"]
            food.color(random.choice(colors))
            for part in body_parts:
               part.goto(2000,2000)
            #part.hideturtle()
            body_parts.clear()
            score=0
            delay=0.1
            pen.clear()
            pen.write("Score:{}  High score:{}".format(score,high_score),align="center",font=("courier","24","bold"))

