import turtle

dizzly=turtle.Turtle()
dizzly.shape("turtle")
def dizzlyisdizzy(length):
    while True:
        if length<300:
            dizzly.forward(5+length)
            dizzly.left(90)
            dizzlyisdizzy(length+5)
        
dizzlyisdizzy(5 )