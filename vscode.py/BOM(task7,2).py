import random

chosse=random.randint(0,10)

turn=1
while True:
    if chosse%2==0:
        chosse+=1
        if turn%5==0:
            print("computer: BOM")
            turn+=1
        else :
            print("computer: ",turn)
            turn+=1

    else :
        
        chosse+=1
        if turn%5==0  :
            user=input("user: ").upper()
            if user=="BOM":
                turn+=1

            else:
                print("haaha u lost u loser")
                break

        else :
            user=int(input("user: "))
            if turn==user:
                turn+=1

            else:
                print("haaha u lost u loser")
                break


        
