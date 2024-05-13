list1=input("enter a word: ").split(",")
v="**"+"*"*len(list1[0])
print(v)

for e in list1:
    print("*" + e + "*")

print(v)

