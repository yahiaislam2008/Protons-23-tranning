import random

i=random.randrange(1 , 50)
print(i)

while True:


    n=int(input("Enter your guess: "))

    while i!=n:
        
        print("your guess is :" , n)


        if i > n :
            print("A bit too high")
            n=int(input("Enter your guess: "))


        if i < n :
            print("A bit too low")
            n=int(input("Enter your guess: "))

        #if i in range(n(i +4)):
        #   print("close")

        #if i in range(n(i -4)):
        #   print("close")

    if i == n:

        print("u got it!")
        break
