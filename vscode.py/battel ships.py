print("welcome to the game of battel ships!!!")
grid=int(input("Enter the grid size(diffuclty level)?!: "))
print("u have 5 turns")

p="O "*grid+"\n"

l=[p]

for i in range(1):
    import random
    ship_r=random.randint(0,grid)
    ship_c=random.randint(0,grid)
    ship=(ship_c,ship_r)
for i in range(5):
    if grid<=5:
        if grid==1:
            for i in range(1):
                print(p)

        for i in range(grid):
            print(p)
    guess_r=int(input("enter your hit in row: "))
    guess_c=int(input("enter your hit in colmun: "))
    guess=(guess_c,guess_r)
    #guess.split(",")
    g=[]
    
    if guess==ship:
        print("u got it !")
        break
    

    elif guess>ship or guess<ship and guess not in g :
        print("u missed")
        g.append(guess) 
        continue 

    elif guess in g :
        print("already hit")


    