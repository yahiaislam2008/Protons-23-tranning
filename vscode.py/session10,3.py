def star(level):
    if level ==1:
        return "*"
    else:
        #level*"*"
        return  level*"*", star(level-1)

#print(10*"*")
level=int(input("Enter level of stars: "))
print(star(level))
