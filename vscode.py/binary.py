def find( decimal_number ):
    if decimal_number == 0:
        return 0
    return (decimal_number % 2 + 10 *find(decimal_number // 2))
 
decimal_number = int(input("Enter a good numbers: "))
print(find(decimal_number))