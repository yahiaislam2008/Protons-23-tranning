import sys
sys.setrecursionlimit(3000)
def factorial(num):
    if num ==1 :
        return 1
    
    else:
        
        sum=factorial(num-1)
        return sum*num



while True:
    x=int(input("Enter a number: "))
    print(factorial(x))
