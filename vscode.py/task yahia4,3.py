import random
 
uppeercase_chacter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_chacter="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
symbols="()[]{}!@#.,/\\*-_+:;? "



upper ,lower, nums, syms= True , True , True , True

all=" "

if upper:
    all +=uppeercase_chacter

if lower:
    all +=lowercase_chacter

if nums:
    all +=digits

if syms:
    all +=symbols


length =15

amount =int(input("enter amount:"))


for x in range(amount):
    password=" ".join(random.sample(all, length))
    print(password)



