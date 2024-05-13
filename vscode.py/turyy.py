from turtle import Turtle


side=int(input("Enter the number of the side: "))
n=side*2
s=((180*(n-2))/n)
mt=Turtle()
mt.shape("turtle")
mt.color("yellow")
for i in range(side):
    mt.forward(60)
    mt.left(s)
    mt.left(s)
