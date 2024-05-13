import turtle

def tree(branchlen,depth):
    if depth ==0:
        return
    mytree.forward(branchlen)
    mytree.left(45)
    tree(branchlen/1.6,depth-1)
    mytree.right(90)
    tree(branchlen/1.6,depth-1)
    mytree.left(45)
    mytree.backward(branchlen)





mytree=turtle.Turtle()
mytree.shape("turtle")
mytree.speed(0)

window=turtle.Screen()

window.bgcolor("gray")

mytree.penup()
mytree.right(90)
mytree.forward(400)
mytree.pendown()
mytree.left(180)

tree(300,10)

window.exitonclick()