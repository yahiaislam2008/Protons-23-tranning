import turtle
sier=turtle.Turtle()
sier.shape("turtle")

def sierpinski(length, depth):
    if depth==0:
        for _ in range(3):
            sier.fd(length)
            sier.lt(120)
    else:
        sierpinski(length/2, depth-1)
        sier.forward(length/2)
        sierpinski(length/2, depth-1)
        sier.backward(length/2)
        sier.left(60)
        sier.forward(length/2)
        sier.right(60)
        sierpinski(length/2, depth-1)
        sier.left(60)
        sier.backward(length/2)
        sier.right(60)


sier.speed(0)
sier.penup()
sier.goto(-200,-200)
sier.pendown()

sierpinski(500,6)
turtle.done()