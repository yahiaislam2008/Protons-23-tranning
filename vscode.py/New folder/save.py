import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Score Tracker")
wn.bgcolor("white")
wn.setup(width=600, height=400)

# Initialize variables
score = 0
high_score = 0

# Load the high score from a file if it exists
try:
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    pass

# Create the turtle for displaying the score
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color("black")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 150)
score_turtle.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Function to update the score
def update_score(points):
    global score, high_score
    score += points
    if score > high_score:
        high_score = score
        with open("high_score.txt", "w") as file:
            file.write(str(high_score))
    score_turtle.clear()
    score_turtle.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Keyboard bindings
def increase_score():
    update_score(10)

wn.listen()
wn.onkeypress(increase_score, "space")

# Main game loop
while True:
    wn.update()