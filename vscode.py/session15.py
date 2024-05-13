listnum=input("Enter number for list between every number comma: ").split(",")
print(*listnum)
number=int(input("Enter a number: "))
big=0
for num in range(0,len(listnum)):
    if int(listnum[num]) > number:
        big += 1
print(big)        

        
    