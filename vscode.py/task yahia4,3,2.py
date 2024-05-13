import secrets
import string
import random


upper=string.ascii_uppercase
lower=string.ascii_lowercase
nums=string.digits
syms=string.punctuation
all= upper + lower + nums + syms

password=""


uppercase=int(input("enter number of upper characters:"))
lowcase=int(input("enter number of lower characters:"))
digits=int(input("enter numbers of digits characters:"))
symblos=int(input("enter numbers of special characters:"))

for i in range(uppercase):
    password +="".join(random.choice(secrets.choice(upper)))

for i in range(lowcase):
    password +="".join(random.choice(secrets.choice(lower)))

for i in range(digits):
    password +="".join(random.choice(secrets.choice(nums)))

for i in range(symblos):
    password +="".join(random.choice(secrets.choice(syms)))

remaining =uppercase - lowcase - digits - symblos

for i in range(remaining):
    password +="".join(random.choice(secrets.choice(all)))

password=list(password)
random.shuffle(password)
print("".join(password))