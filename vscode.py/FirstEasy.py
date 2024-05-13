x=int(input("Enter Your Num: "))

if x in range(6,21):
    print("it is weird")
elif x%2==0:
    print("It's Not Weird")
else:
    print("It's Weird")
