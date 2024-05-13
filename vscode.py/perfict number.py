def perfuct_number(num):
    sum=0
    for number in range (1,num): 
        if num % number==0:
            sum=sum+number

    if num==sum:
        return True 
    else :
        return False
    
num=int(input("Enter a number: "))
print(perfuct_number(num))


def perfiect_number(n):
    div=[i for i in range (1,n) if n%i==0]
    
    return n==sum(div)
        
for i in range(1,10000+1):
    if perfiect_number(i):
        print(i ,end="\n")


