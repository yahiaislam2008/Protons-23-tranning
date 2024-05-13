import random
#user=int(input("user: "))
tu=(1,0)
counter=1
turn=random.choice(tu)
#if ==counter:
    #turn= 1
while True:
    if turn==1:
        computer=counter
        if computer==counter:
            print("computer: ",computer)
            computer=counter+1
            turn=0
        elif computer%5==0:
            print("computer: BOM")
            turn=0
            counter=counter+1

        else:
            print("computer:",computer)
            turn =0
            counter=counter+1

    elif turn==0:
        user=int(input("user: "))
        #if user%5==0 and user =="BOM":
            #   turn=1
            #  counter=counter+1
        #else :
            #   print("u lose")
        if user==counter:
            counter=counter+1
            turn=1    
        elif user==counter+1:
                
            counter=counter+1
            turn=1
        else:
            print("u lose")
            break
#else :
 #   print("u lose")

