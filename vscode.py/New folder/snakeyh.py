import turtle
import random
import time
import winsound
import pickle
import os
import json
with open("players.json") as f:
    data=json.load(f)
    
os.system("cls")

player1 = input("Enter your username: ")
player2 = input("Enter your username: ")

delay = 0.1
score1 = 0
score2 =0
high_score=0
yahiafile = open("data.obj", "rb")
high_score = pickle.load(yahiafile)
yahiafile.close()
window = turtle.Screen()
window.title("Snake🐍")
window.bgcolor("#000087")
window.setup(width=600, height=600)
window.cv._rootwindow.resizable(False,False)
window.tracer(0)

head1 = turtle.Turtle()
head1.shape("circle")
head1.color("white")
head1.penup()
head1.speed(0)
head1.goto(0, 50)
head1.direction = "stop"
head2 = turtle.Turtle()
head2.shape("circle")
head2.color("white")
head2.penup()
head2.speed(0)
head2.goto(0, -50)
head2.direction = "stop"

food = turtle.Turtle()
colors = random.choice(["red", "black", "green"])
shapes = random.choice(["circle", "square"])
food.color(colors)
food.shape(shapes)
food.penup()
food.speed(0)
x = random.randrange(-260, 260)
y = random.randrange(-260, 260)
food.goto(x, y)

pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.goto(0, 270)
pen.write(player1 +":0      Highscore:{}".format(high_score),align="center", font=("arial", 24, "bold"))
pen2 = turtle.Turtle()
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.speed(0)
pen2.hideturtle()
pen2.goto(0, -280)
pen2.write(player2 +":0      Highscore:{}".format(high_score),align="center", font=("arial", 24, "bold"))
def go_up():
    if head1.direction != "Down":
        head1.direction = "Up"


def go_down():
    if head1.direction != "Up":
        head1.direction = "Down"


def go_right():
    if head1.direction != "Left":
        head1.direction = "Right"


def go_left():
    if head1.direction != "Right":
        head1.direction = "Left"


def move():
    if head1.direction == "Up":
        y = head1.ycor()
        head1.sety(y+20)
    if head1.direction == "Down":
        y = head1.ycor()
        head1.sety(y-20)
    if head1.direction == "Left":
        x = head1.xcor()
        head1.setx(x-20)
    if head1.direction == "Right":
        x = head1.xcor()
        head1.setx(x+20)


window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")

def goup1():
    if head2.direction != "s":
        head2.direction ="w"

def godown1():
    if head2.direction != "w":
        head2.direction ="s"

def goleft1():
    if head2.direction != "d":
        head2.direction ="a"

def goright1():
    if head2.direction != "a":
        head2.direction ="d"

def move1():
    if head2.direction == "w":
        y = head2.ycor()
        head2.sety(y+20)
    if head2.direction == "s":
        y = head2.ycor()
        head2.sety(y-20)
    if head2.direction == "a":
        x = head2.xcor()
        head2.setx(x-20)
    if head2.direction == "d":
        x = head2.xcor()
        head2.setx(x+20)

window.listen()
window.onkeypress(goup1, "w")
window.onkeypress(godown1, "s")
window.onkeypress(goright1, "d")
window.onkeypress(goleft1, "a")

body_parts1 = []
body_parts2 = []
def losing1():
        time.sleep(1)
        head1.goto(0, 50)
        head1.direction = "Stop"
        colors = (["red", "orange", "purple"])
        food.color(random.choice(colors))
        for part in body_parts1:
            part.goto(1000, 1000)
            part.hideturtle()
        body_parts1.clear()

def losing2():
        time.sleep(1)
        head2.goto(0, -50)
        head2.direction = "Stop"
        colors = (["red", "orange", "purple"])
        food.color(random.choice(colors))
        for part in body_parts2:
            part.goto(1000, 1000)
            part.hideturtle()
        body_parts2.clear()

winsound.PlaySound("5d8dca9b-72af-4d70-b939-94f023204031.wav", winsound.SND_ASYNC)
while True:

    yahiafile = open("data.obj", "rb")
    high_score = pickle.load(yahiafile)
    yahiafile.close()
    window.update()
    if head1.ycor() > 275 or head1.ycor() < -275 or head1.xcor() > 275 or head1.xcor() < -275:
        winsound.PlaySound("mixkit-horror-lose-2028.wav", winsound.SND_ASYNC)
        losing1()
       # time.sleep(1)
 #       head1.goto(0, 50)
  #      head1.direction = "Stop"
   #     colors = (["red", "orange", "purple"])
    #    food.color(random.choice(colors))
     #   for part in body_parts1:
      #      part.goto(1000, 1000)
       #     part.hideturtle()
        #    body_parts1.clear()
        score1 = 0
        delay = 0.1
        pen.clear()
        pen.write(player1+":{}  Highscore:{}".format(score1, high_score),align="center", font=("courier", "24", "bold"))

    if head2.ycor() > 275 or head2.ycor() < -275 or head2.xcor() > 275 or head2.xcor() < -275:
        winsound.PlaySound("mixkit-horror-lose-2028.wav", winsound.SND_ASYNC)
        losing2()
#        time.sleep(1)
 #       head2.goto(0, -50)
  #      head2.direction = "Stop"
   #     colors = (["red", "orange", "purple"])
    #    food.color(random.choice(colors))
     #   for part in body_parts2:
      #      part.goto(1000, 1000)
       #     part.hideturtle()
        #body_parts2.clear()
        score2 = 0
        delay = 0.1
        pen2.clear()
        pen2.write(player2+":{}  Highscore:{}".format(score2, high_score),align="center", font=("courier", "24", "bold"))

    if head1.distance(food) < 20:
        winsound.PlaySound("mixkit-arcade-retro-run-sound-220.wav", winsound.SND_ASYNC)
        x = random.randrange(-260, 260)
        y = random.randrange(-260, 260)
        food.goto(x, y)
        shapes = random.choice(["circle", "square"])
        food.shape(shapes)
        colors = (["red", "orange", "purple", "green", "yellow"])
        food.color(random.choice(colors))
        new_part = turtle.Turtle()
        new_part.shape("circle")
        new_part.color("orange")
        new_part.speed(0)
        new_part.penup()
        body_parts1.append(new_part)
        delay -= 0.001
        score1 += 10
        if score1 > high_score:
            high_score = score1
        pen.clear()
        pen.write(player1+":{}  Highscore:{}".format(score1, high_score),align="center", font=("courier", "24", "bold"))
    for index in range(len(body_parts1)-1, 0, -1):
        x = body_parts1[index - 1].xcor()
        y = body_parts1[index - 1].ycor()
        body_parts1[index].goto(x, y)
    if len(body_parts1) > 0:
        x = head1.xcor()
        y = head1.ycor()
        body_parts1[0].goto(x, y)
    move()

    if head2.distance(food) < 20:
        winsound.PlaySound("mixkit-arcade-retro-run-sound-220.wav", winsound.SND_ASYNC)
        x = random.randrange(-260, 260)
        y = random.randrange(-260, 260)
        food.goto(x, y)
        shapes = random.choice(["circle", "square"])
        food.shape(shapes)
        colors = (["red", "orange", "purple", "green", "yellow"])
        food.color(random.choice(colors))
        new_part = turtle.Turtle()
        new_part.shape("circle")
        new_part.color("orange")
        new_part.speed(0)
        new_part.penup()
        body_parts2.append(new_part)
        delay -= 0.001
        score2 += 10
        if score2 > high_score:
            high_score = score2
        pen2.clear()
        pen2.write(player2+":{}  Highscore:{}".format(score2, high_score),align="center", font=("courier", "24", "bold"))

    for index in range(len(body_parts2)-1, 0, -1):
        x = body_parts2[index - 1].xcor()
        y = body_parts2[index - 1].ycor()
        body_parts2[index].goto(x, y)
    if len(body_parts2) > 0:
        x = head2.xcor()
        y = head2.ycor()
        body_parts2[0].goto(x, y)
    move1()

    for part in body_parts1:
        if part.distance(head1) < 20:
            losing1()
#            time.sleep(1)
 #           head1.goto(0, 50)
  #          head1.direction = "Stop"
   #         colors = (["red", "orange", "purple"])
    #        food.color(random.choice(colors))
     #       for part in body_parts1:
      #          part.goto(1000, 1000)
            # part.hideturtle()
       #     body_parts1.clear()
            score1 = 0
            delay = 0.1
            pen.clear()
            pen.write(player1+":{}  Highscore:{}".format(score1, high_score),align="center", font=("courier", "24", "bold"))
    #time.sleep(delay)
    for part in body_parts2:
        if part.distance(head2) < 20:
            losing2()
#            time.sleep(1)
 #           head2.goto(0, 0)
  #          head2.direction = "Stop"
   #         colorss = (["red", "orange", "purple"])
    #        food.color(random.choice(colors))
     #       for part in body_parts2:
      #          part.goto(1000, 1000)
            # part.hideturtle()
       #     body_parts2.clear()
            score2 = 0
            delay = 0.1
            pen2.clear()
            pen2.write(player2+":{}  Highscore:{}".format(score2, high_score),align="center", font=("courier", "24", "bold"))

    
    for part in body_parts1:
        if part.distance(head2)<20:
            losing2()
            score2 = 0
            delay = 0.1
            pen2.clear()
            pen2.write(player2+":{}  Highscore:{}".format(score2, high_score),align="center", font=("courier", "24", "bold"))

    for part in body_parts2:
        if part.distance(head1)<20:
            losing1()
            score1 = 0
            delay = 0.1
            pen.clear()
            pen.write(player1+":{}  Highscore:{}".format(score1, high_score),align="center", font=("courier", "24", "bold"))
    time.sleep(delay)
    yahiafile = open("data.obj", "wb")
    pickle.dump(high_score, yahiafile)
    yahiafile.close()

# By team 7-strange codes:
    # 1:Farida Mohamed
    # 2:Omar Tharwat
    # 3:Yahia Islam