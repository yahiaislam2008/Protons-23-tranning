def maximaum(y,x,u):
    if x>y and x>u:
        return x
    elif y>x and y>u:
        return y
    elif u>x and u>y:
        return u



y=int(input("enter the 1st number: "))
x=int(input("enter the 2nd number: "))
u=int(input("enter the 3th number: "))

print(maximaum(y,x,u))


