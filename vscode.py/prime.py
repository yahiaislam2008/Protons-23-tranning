x =int(input("enter your number: "))
prime ="prime"
if x ==1:
    prime="not prime"
    print(prime)

for i in range(2,x):
    if x%i==0:
        
        print("not prime")
        break

print(prime)