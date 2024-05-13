import random

weapons=("r","p","s")
play=True
while play:
    #player=None
    computer=random.choice(weapons)
    player=input("choose your weapon: [R]ock] , [P]aper ,or[S]cissor: ").lower()
    while player not in weapons:
        print("shows from weapons only")
        player=input("choose your weapon: [R]ock] , [P]aper ,or[S]cissor: ").lower()
        
    print(f"u chose:{player}")
    print(f"i chose:{computer}")
    if player==computer:
        print("Tie !")

    elif player=="r":
        if computer=="p":
            print("haa u lost")
        
        elif computer=="s":
            print("Ok u won")

    elif player=="p":
        if computer=="s":
            print("haha u lost")
        
        elif computer=="r":
            print("Ok u won")

    elif player=="s":
        if computer=="r":
            print("haa u lost")
        
        elif computer=="p":
            print("Ok u won")
    yorn=("yes","no")
    #choose=input("Do u want to play with me again u scary cat (Yes/No): ").lower()
    #if play =="yes":
     #   play=False
   # while choose not in yorn:
    
    choose=input("Do u want to play with me again(Yes/No): ").lower()
        #if not choose =="yes":
         #   play=False
    if choose not in yorn:
        while True:
            print("Yes or No only")           
            choose=input("Do u want to play with me again u scary cat (Yes/No): ").lower()
            if choose =="no":
                play=False  
                break
    if choose =="no":
        play=False 

print("Thanks for playing with me scary cat")