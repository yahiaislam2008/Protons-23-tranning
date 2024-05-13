#import json
data = {}
while True:
    print("choose what would you like to do")
    user=int(input("1.login \n2.Regist \n3.Exit"))
    if user==1:
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        if password ==data[username]["pass"]:
            
            print("\nwelcome back :username")
            print(username)
            print("your secret is : " , data[username]["secret"])
            continue
        else:
            print("error:  incorrect password")
    elif user==2:
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        secret=input("Enter your secret: ")
        data[username] = {"pass": password ,"secret": secret}
        print(data)
        print("u have succefully regrest")
    elif user ==3:
            print("bye see u next time")
            break
    
         #print
        #data[username] = {"pass": password ,"secret": secret}
        #print (data)

        #if data[username]==username and username[password]==password:
        #print(secret)
        #with open ('person.txt', 'w') as f:
    #json.dump(data, f)