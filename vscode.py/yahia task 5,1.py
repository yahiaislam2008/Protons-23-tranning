def yahia(x):
    z=x[::-1]
    
    if x != z:
        return"it's not the same"

    elif x == z:
        return"it's the same"

   

x=input("enter your word: ")


print(yahia(x))