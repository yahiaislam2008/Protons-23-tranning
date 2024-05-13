def perfect_number(n):
    divisors=[i for i in range(1,n) if n%i==0 ]
    return n==sum(divisors)

for i in range(1,10000+1):
    if perfect_number(i):
        print(i ,end="\n")