y=int(input("enter a number :"))

prime = 1
for i in range(2 ,y):
    if y%i==0:
      prime = 0
      
if prime == 1 :
    print("this number is prime")
else :
   print("this number is not prime") 