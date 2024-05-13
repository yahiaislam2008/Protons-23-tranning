import turtle

mt=turtle.Turtle()


def tree(depth , length):

    if depth==0:
        return

    else:




        mt.left(45)
        mt.forward(length//2)
        tree(depth -1,length//2)

        mt.backward(length//2)
        mt.rigth(90)
        mt.forward(length//2)
        tree(depth -1,length//2)


        mt.backward(length//2)
        mt.right(45)

length=200
mt.left(90)
mt.backward(400)
mt.forward(400)
tree(6,400)


