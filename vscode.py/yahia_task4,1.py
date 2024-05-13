import random

g=list(range(0,50+1))
i=""
i =random.choice(g)
for i in g:
   
    u=("the random number is between 1 and 50 can you guess it?")
    print(u)

    z=int(input("enter your guess:"))

    c=("close")
    a=("a bit too low. try again.")
    e=("a bit too high. try again.")
    #x=15
    #y=list(range(16,20+1))
    #s=list(range(10,14+1))
    #l=list(range(1,9+1))
    #=list(range(21,50+1))
    #print(z)

    if z==g:
      print("u got it!")
      break
#print("u got it!")
   
    #if z==list(range(16,26+1)) or z==list(range(10,14+1)):
    #print(c)
    if g > z or g < z:
        
        print("close")
    
    #elif z==list(range(1,9+1)):
    #print(a)
    #if z:
       
     #   print("a bit too low. try again.")
        #print(a)
         
    #elif z==list(range(27,50+1)):\
    #print(h)
    #if z==h:

     #   print("a bit too high. try again.")  
                
#if z==x:
       #break
#print("u got it!")
#print("u got it!")
    
       
