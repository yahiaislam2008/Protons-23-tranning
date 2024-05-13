odd=[]
even=[]
x=int(input("Enter Your Number, enter 0 if u fineshed: "))
while not x==0:
    x=int(input("Enter Your Number, enter 0 if u fineshed: "))
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
if len(even)>len(odd):
    print("The even numbers win!")
elif len(odd)>len(even):
    print("The odd numbers win!")
else:
    print("tie!")