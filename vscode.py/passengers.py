stations=int(input("Enter number of statons: "))
paseengers=0
passenger=int(input("enter passengers: "))
paseengers += passenger
print("her is the number of passengers:\n>",paseengers)
def train(stations):
    global paseengers
    stations -= 1
    while stations > 0:
        stations -= 1
        passenger=int(input("enter passengers: "))
        paseengers +=passenger
        outs=int(input("enter outs: "))
        # outs > paseengers:
        if  outs > paseengers :  
            while outs > paseengers :
                print("Enter a number in range the passengers please: ")
                outs=int(input("enter outs: "))
        else:            
            paseengers -=outs
            print("her is the number of passengers:\n>",paseengers)
        
print(train(stations))