def border_msg(msg):
    row = len(msg)
    columns = len(msg[0])
    h = ' '.join(['+'] + ['-' *columns] + ['+'])
    result = [h] + [msg] + [h]
    return result
#msg=input("Enter a word: ")
print(border_msg("hello"))

r=int(input("Enter the number of row: "))

c=int(input("Enter the number of colums: "))



for i in range(r):
    for j in range(c):
        if i==0 or i==(r-1) or j==0 or j==(c-1):
            
            print("+",end=" ")
        else:
            print(" ",end=" ")
       
    print( )

def reverse(num):
  rev = 0
  while(num != 0):
      reminder = num % 10
      rev = (rev * 10 ) + reminder
      num = num // 10 
  print ("Reverse number is  : " , rev )
 
num=input("enter number : ")
reverse(int(num))


num = int(input("So you like things backwards eh? Well, enter a number and I'll do my best: "))
Onum = str(num)
revStr = ""
for x in Onum:
  revStr = x + revStr

print("Your wish is my command! Your" , num, "looks like", revStr, "Backwards!")






n=int(input("Enter a number: "))
rev=0
def yahia1(n):
    global rev
    if n>0:
        r=n %10
        rev=(rev *10) + r
        yahia1(n //10)
    return rev
rev=yahia1(n)
print("the reversed number is: %d"%rev)




h=input("enter your word: ")
i=len(h)
y="-"*i
print("+ "+ y +" +" +"\n"+ "| " + h +" |"+"\n"+ "+ "+ y +" +")   


for Number in range(1, 1000 - 1):
    Sum = 0
    for n in range(1, Number - 1):
        if(Number % n == 0):
            Sum = Sum + n
            
    # display the result
    if(Sum == Number):
        print(Number)

def Perfect_Number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return n == sum(divisors)

for i in range(1, 1001):
    if Perfect_Number(i):
        print(i, end= '\n')



hard=int(input("en: "))
i=hard
h="0  "*i+"\n"

if hard==1:
    print(h)
elif hard==2:
    print(h+h)
elif hard==3:
    print(h+h+h)
elif hard==4:
    print(h+h+h+h)
elif hard==5:
    print(h+h+h+h+h)
elif hard==6:
    print(h+h+h+h+h+h)
elif hard==7:
    print(h+h+h+h+h+h+h)
elif hard==8:
    print(h+h+h+h+h+h+h+h)