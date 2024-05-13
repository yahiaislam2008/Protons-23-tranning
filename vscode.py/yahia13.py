def encript(word,x):
    string=" "
    for i in range(0,len(word)):
        
   
        y=ord(word[i])+x
        c=chr(y)
        string+=c

    return string
word=input("enter your password: ")
x=int(input("enter a number: "))
print(encript(word,x))