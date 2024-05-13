

def yahia():
    y=input("Enter a password: ")
    s=int(input("Enter a number: "))
    for i in range(0, len(y)):
        
        d = ord(y[i])
        u=chr(d)+s
        y[i]= d
        
    return y
print(yahia())

     