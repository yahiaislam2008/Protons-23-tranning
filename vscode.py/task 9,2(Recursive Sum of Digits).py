def sums(n):
    if n < 10:
        return n
    return n % 10 + sums(n // 10)

number= int(input("Enter a good numbers: "))
print("your sum digits is: ",sums(number))