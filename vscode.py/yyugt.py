import turtle

# ====================== Window Setup ======================
window = turtle.Screen()
window.title("Pong")
window.setup(width=800, height=600)
window.tracer(0)  # set delay for update drawings
window.bgcolor(0.1, 0.1, 0.1)

# ================= Game Objects Setup =================
# ball
ball = turtle.Turtle()
ball.speed(0)  # drawing speed (fastest)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)

# these variables determine the direction of the ball
# in the x-axis and y-axis respectively, they both can only be either 1 or -1
ball_dx = 1
ball_dy = 1

# play around with this value until the game is playable
ball_speed = 0.05

# center line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.color("white")
center_line.penup()
center_line.goto(0, 300)
center_line.pendown()
center_line.goto(0, -300)

# player1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.color("red")
player1.penup()
player1.goto(-350, 0)

# player2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.color("blue")
player2.penup()
player2.goto(350, 0)

p1_score = 0
p2_score = 0
score = turtle.Turtle()
score.color("white")
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player1: 0 Player2: 0", align="center", font=("Courier", 20, "bold"))

# ==================== Players Movement ====================

# play around with this value until the game is playable
players_speed = 20

# Function to move the left paddle up
def movePad1Up():
    y = player1.ycor()  # Getting the current y-coordinate of the left paddle
    y += players_speed
    player1.sety(y)  # Updating the y-coordinate of the paddle

# Function to move the left paddle down
def movePad1Down():
    y = player1.ycor()  # Getting the current y-coordinate of the left paddle
    y -= players_speed
    player1.sety(y)  # Updating the y-coordinate of the paddle

# Function to move the right paddle up
def movePad2Up():
    y = player2.ycor()  # Getting the current y-coordinate of the right paddle
    y += players_speed
    player2.sety(y)  # Updating the y-coordinate of the paddle

# Function to move the right paddle down
def movePad2Down():
    y = player2.ycor()  # Getting the current y-coordinate of the right paddle
    y -= players_speed
    player2.sety(y)  # Updating the y-coordinate of the paddle


# Matching the Keyboard buttons to the above functions
window.listen()
window.onkeypress(movePad1Up, "w")
window.onkeypress(movePad1Down, "s")
window.onkeypress(movePad2Up, "Up")
window.onkeypress(movePad2Down, "Down")

#The main game
while True:
    #Updating the screen every time with the new changes
    window.update()

    #Moving the ball by updating the coordinates
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # Checking if ball hits the top of the screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1  # Bouncing the ball

    # Checking if ball hits the bottom of the screen
    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1  # Bouncing the ball

    # Checking if the ball hits the left or right walls, the player missed the hit
    if ball.xcor() > 390:
        p1_score += 1  # Increasing the score of player 1 if player 2 missed
        score.clear()
        score.write("Player1: {} Player2: {}".format(p1_score, p2_score), align="center", font=("Courier", 20, "bold"))
        ball.goto(0, 0)
        ball_dx *= -1
        ball_dy *= -1
    elif ball.xcor() < -390:
        p2_score += 1