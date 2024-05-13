import turtle 
import random 
import time
import winsound



player=input("Enter your username: ")
delay=0.1
score=0
high_score=0


window=turtle.Screen()
window.title("Snake🐍")
window.bgcolor("#000087")
window.setup(width=600,height=600)
#window.cv._rootwindow.resizable(False,False)
window.tracer(0)

head=turtle.Turtle()
head.shape("circle")
head.color("white")
head.penup()
head.speed(0)
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
colors=random.choice(["red","black","green"])
shapes=random.choice(["circle","square"])
food.color(colors)
food.shape(shapes)
food.penup()
food.speed(0)
food.goto(0,100)

pen=turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.goto(0,260)
pen.write(player+":0  High score:0",align="center",font=("courier",24,"bold"))

def go_up():
    if head.direction !="Down":
        head.direction ="Up"

        
def go_down():        
    if head.direction !="Up":
        head.direction= "Down" 

def go_right() :       
    if head.direction !="Left":
        head.direction ="Right"


def go_left():
    if head.direction !="Right":
        head.direction ="Left"
 
def move():
    if head.direction == "Up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "Down":
        y=head.ycor()
        head.sety(y-20) 
    if head.direction == "Left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction == "Right":
        x=head.xcor()
        head.setx(x+20)


window.listen() 
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")  
window.onkeypress(go_right, "Right") 
window.onkeypress(go_left, "Left") 

body_parts=[]
winsound.PlaySound("5d8dca9b-72af-4d70-b939-94f023204031.wav", winsound.SND_ASYNC) 
while True:
      window.update() 
      if head.ycor()>310  or head.ycor()<-310  or head.xcor()>310  or head.xcor()<-310:
        winsound.PlaySound("mixkit-horror-lose-2028.wav", winsound.SND_ASYNC)
        time.sleep(1)
        head.goto(0,0)
        head.direction="Stop"
        colors=(["red","orange","purple"])
        food.color(random.choice(colors))
        for part in body_parts:
            part.goto(1000,1000)
            part.hideturtle()
        body_parts.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write(player+":{}  High score:{}".format(score,high_score),align="center",font=("courier","24","bold"))

      if head.distance(food) < 20 :
        winsound.PlaySound("mixkit-arcade-retro-run-sound-220.wav",winsound.SND_ASYNC)
        x=random.randrange(-270,270)
        y=random.randrange(-270,270)
        food.goto(x,y)
        shapes=random.choice(["circle","square"])
        food.shape(shapes)
        colors=(["red","orange","purple","green","yellow"])
        food.color(random.choice(colors))
        new_part=turtle.Turtle()
        new_part.shape("circle")
        new_part.color("orange")
        new_part.speed(0)
        new_part.penup()
        body_parts.append(new_part)
        delay -=0.001
        score +=10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(player+":{}  High score:{}".format(score,high_score),align="center",font=("courier","24","bold"))

      for index in range(len(body_parts)-1 ,0 ,-1):
        x=body_parts[index -1].xcor()
        y=body_parts[index -1].ycor()
        body_parts[index].goto(x,y)
      if len(body_parts)>0:
        x=head.xcor()
        y=head.ycor()
        body_parts[0].goto(x,y)
      move()
      for part in body_parts:
        if part.distance(head) < 20 :
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
            pen.write(player+":{}  High score:{}".format(score,high_score),align="center",font=("courier","24","bold"))


      time.sleep(delay)





#By team 7-strange codes:
    #1:Farida Mohamed
    #2:Omar Tharwat
    #3:Yahia Islam