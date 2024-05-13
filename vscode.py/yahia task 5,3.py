n=int(input("Enter a number: "))
reverse=0
def yahia1(n):
    global reverse
    if n>0:
        r=n %10
        reverse=(reverse *10) + r
        yahia1(n //10)
    return reverse
reverse=yahia1(n)
print("the reversed number is: %d"%reverse)
