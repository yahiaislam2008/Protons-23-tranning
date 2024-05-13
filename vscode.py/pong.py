import turtle

# ====================== Window Setup ======================
window = turtle.Screen()
window.title("Pong")
window.setup(width=800, height=600)
window.tracer(0)  # set delay for update drawings
window.bgcolor(.1, .1, .1)

# ================= Game Objects Setup =================
# ball
ball = turtle.Turtle()
ball.speed(0)  # darwing speed(fastest)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
# TODO: Continue setup

# these variables determine the direction of the ball
# in the x-axis and y-axis respectively, they both can only be either 1 or -1
ball_dx = 1
ball_dy = 1

# play around with this value until the game is playable
ball_speed = 0.5

# center line
line = turtle.Turtle()
line.goto(0,0)
line.shape("square")
line.color("white")
line.shapesize(stretch_len=0.1,stretch_wid=30)


# TODO: Setup a center line that divides the screen

# player1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.color("red")
player1.penup()
player1.goto(-300, 0)
# TODO: Continue setup

# player2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.color("blue")
player2.penup()
player2.goto(300, 0)
# TODO: Continue setup

p1_score = 0
p2_score = 0
score = turtle.Turtle()
score.color("white")
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player1 : 0 Player2: 0", align="center", font=("Courier", 20, "bold"))
# score text
# TODO: Setup a text turtle at the top of the screen to display the score

# variables to hold player 1 & player 2 scores

# ==================== Players Movement ====================

# play around with this value until the game is playable
players_speed = 20


# Function to move the left paddle up
def movePad1Up():
     y = player1.ycor() #Getting the current y-coordinated of the left paddle
     y += 15
     player1.sety(y) #Updating the y-coordinated of the paddle

# Function to move the left paddle down
def movePad1Down():
    y = player1.ycor()#Getting the current y-coordinated of the left paddle
    y -= 15
    player1.sety(y)#Updating the y-coordinated of the paddle

# Function to move the right paddle up
def movePad2Up():
    y = player2.ycor()#Getting the current y-coordinated of the right paddle
    y += 15
    player2.sety(y)#Updating the y-coordinated of the paddle

# Function to move the right paddle down
def movePad2Down():
   y = player2.ycor()#Getting the current y-coordinated of the right paddle
   y -= 15
   player2.sety(y)#Updating the y-coordinated of the paddle


# Matching the Keyboard buttons to the above functions=
window.listen()
window.onkeypress(movePad1Up, "w")
window.onkeypress(movePad1Down, "s")
window.onkeypress(movePad2Up, "Up")
window.onkeypress(movePad2Down, "Down")

# TODO: Write the player movement functions and bind them to keys


#The main game
while True:
    #Updating the screen ev`ery time with the new changes
    window.update()
    #Moving the ball by updating the coordinates
    ball.setx(ball.xcor()+ball_dx)
    ball.sety(ball.ycor()+ball_dy)

    # Checking if ball hits the top of the screen
    if ball.ycor() > 280:
        ball.sety(280)
        ball_dy *= -1 #Bouncing the ball

    # Checking if ball hits the bottom of the screen
    if ball.ycor() < -280:
        ball.sety(-280)
        ball_dy *= -1#Bouncing the ball

    #Checking if the ball hits the left or right walls, the player missed the hit
    if ball.xcor() > 480 or ball.xcor() < -480:
        if(ball.xcor() <-480):
            p2_score += 1 #Increasing the score of right player if left player missed
    else:
        p1_score += 1 #Increasing the score of left player if right player missed
    #Starting ball again from center towards the opposite direction
        ball.goto(0, 0)
        ball_dx *= -1
        ball_dy *= -1

    #Updating score in the scoreboard
    score.clear()
    score.write("Player1 : {} Player2: {}".format(player1, player2), align="center", font=("Courier", 20, "bold"))

    #Checking if the left player hit the ball
    if (ball.xcor() < -360 and ball.xcor() > -370) and (player1.ycor() + 50 > ball.ycor() > player1.ycor() - 50):
    #Increasing score of left player and updating score board
        player1 += 1
        score.clear()
        score.write("Player A: {} Player B: {}".format(player1, player2), align="center", font=("Courier", 20, "bold"))
        ball.setx(-360)

    #Increasing speed of the ball with the limit 7
    if(ball_dy>0 and ball_dy<5): #If _dy is positive increasing _dy
        ball_dy+=0.5
    elif(ball_dy<0 and ball_dy>-5): #else if _dy is negative decreasing _dy
        ball_dy-=0.5

    if(ball_dx>0 and ball_dx<5):#If _dx is positive increasing _dx
        ball_dx+=0.5
    elif(ball_dx<0 and ball_dx>-5): #else if _dx is negative decreasing _dx
        ball_dx-=0.5

    #Changing the direction of ball towards the right player
    ball_dx *=-1

    #Checking if the right player hit the ball
    if (ball.xcor() > 360 and ball.xcor() < 370) and (player2.ycor() + 50 > ball.ycor() > player2.ycor() - 50):
    #Increasing score of right player and updating scoreboard
        player2 += 1
        score.clear()
        score.write("Player A: {} Player B: {}".format(player1, player2), align="center", font=("Courier", 20, "bold"))
        ball.setx(360)

    #Increasing speed of the ball with the limit 7
    if(ball_dy>0 and ball_dy<7):#If _dy is positive increasing _dy
    
        ball_dy+=1
    elif(ball_dy<0 and ball_dy>-7):#else if _dy is negative decreasing _dy
        ball_dy-=1

    if(ball_dx>0 and ball_dx<7):#If _dx is positive increasing _dx
        ball_dx+=1
    elif(ball_dx<0 and ball_dx>-7): #else if _dx is negative decreasing _dx
        ball_dx-=1

    #Changing the direction of ball towards the left player
    ball_dx*=-1