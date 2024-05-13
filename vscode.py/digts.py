def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

number = int(input("Enter an integer: "))
result = sum_of_digits(number)
print("Sum of digits:", result)