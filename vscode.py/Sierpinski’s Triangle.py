import turtle

def draw_triangle(side_length):
    turtle.forward(side_length)
    turtle.left(120)
    turtle.forward(side_length)
    turtle.left(120)
    turtle.forward(side_length)
    turtle.left(120)

def draw_recursive_triangle(side_length, depth):
    if depth == 0:
        draw_triangle(side_length)
    else:
        draw_recursive_triangle(side_length/2, depth-1)
        turtle.forward(side_length/2)
        draw_recursive_triangle(side_length/2, depth-1)
        turtle.backward(side_length/2)
        turtle.left(60)
        turtle.forward(side_length/2)
        turtle.right(60)
        draw_recursive_triangle(side_length/2, depth-1)
        turtle.left(60)
        turtle.backward(side_length/2)
        turtle.right(60)

turtle.speed(0)  # Set the drawing speed to the fastest
turtle.penup()
turtle.goto(-200, -200)  # Position the turtle to start drawing from the bottom left corner
turtle.pendown()

draw_recursive_triangle(500, 6)  # Change the depth value to adjust the level of recursion

turtle.done()