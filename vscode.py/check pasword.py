def checkpassword(password):
    if len(password)<8:
        return False
    upper = lower =numeric = False
    for ch in password:
        if ch.isupper():
            upper=True
        elif ch.islower():
            lower =True
        elif ch.isnumeric():
            numeric=True
        
    if upper and lower and numeric==True :
        return True
    return False

while True:
    password=input("Enter a password: ")
    print(checkpassword(password))
    break            