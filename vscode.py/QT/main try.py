# while True :
#     n = int(input(">> "))
#     if n%2 == 1:
#         print("A number is weird")
#         continue                                          #1.easy
#     elif n>=6 and n<=20:
#         print("A number is weird")
#         continue
#     else :
#         print("it isn’t weird")
#         continue


# nums = [1,6,8,9,3,10,2,4,7,19,17,13,14,18,32,23,24,29,28]
# odd = []
# even =[]
# for num in nums :
#     if num%2 == 0 :
#         even.append(num)
#     else :
#         odd.append(num)
# print(*even)                      #2.easy
# print(*odd )
# if len(even) > len(odd):
#     print("even wins")
# elif len(even) < len(odd):
#     print("odd wins")
# else :
#     print("tie")

# def appointment(Ta, Td, Tw):
#         if Td > Ta + Tw:
#             return "Late Doctor"
#         else:                                   #3.easy
#             return "Good Doctor"
# # Test the function
# print(appointment(3, 5, 1)) # Output: Late Doctor
# print(appointment(2, 9, 8)) # Output: Good Doctor

_ = input(">> ").split("\n")
