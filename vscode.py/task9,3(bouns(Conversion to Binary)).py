def binarynumber( decimal_number ):
    if decimal_number==0:
        return 0
    return decimal_number%2 +10*(binarynumber(decimal_number//2))

decimal_number=int(input("Enter a number to converted to binary: "))

print("Your decimal number is: ",decimal_number)
print("your binary number is: " , binarynumber(decimal_number))