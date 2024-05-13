from Protons import Protons
from Instructors import Instructors
from Ex_Protons import Ex_Protons
option1=("please chosse which user are u \n 1) Proton \n 2) Instructor \n 3) ExProton")
print(option1)
choice1 =int(input("> "))
users =["Yahia Islam","Farris","Abdallah Elsherbiny","yousef saeed"]
day="sunday"
task="The task is to Use git"
while True :
    if choice1 <4 or choice1 > 0 :
        if choice1 ==1 :
            proton=Protons(input("Enter your username: "),int(input("And age please: ")))
            print(proton.prinformations())
            proton.notifications1()
            proton.notifications2()
            print("\n")
            while True :
                print("chosse what do u want \n 1) View Session \n 2) Add Comment \n 3) View Task \n 4) View Users \n 5) Share Session \n 6) Download Session \n 7) Add Comment on session \n 8) Add Comment on Task \n 9) Solve Task \n 10) Submit Task \n 11) Exit")
                choice2 = int(input(">"))    
                if choice2 <12 or choice2 >0 : 
                    if choice2 ==1 :
                        print("\n")
                        proton.viewSession()
                        print("\n")
                    elif choice2 ==2 :
                        print("\n")
                        massege = input("Enter your comment: ")
                        proton.addcomment()
                        print("\n")
                    elif choice2 ==3:
                        print("\n")
                        task="The task is to Use git"
                        proton.viewTask(task)
                        proton.timeforsubmit(day)
                        print("\n")
                    elif choice2 ==4:
                        print("\n")
                        proton.viewusers(users)
                        print("\n")
                    elif choice2 ==5:
                        print("\n")
                        proton.shareSession()
                        print("\n")
                    elif choice2 ==6:
                        print("\n")
                        proton.downloadSession()
                        print("\n")
                    elif choice2 ==7 :
                        print("\n")
                        massege = input("Enter your comment: ")
                        proton.addcommentonsession()
                        print("\n")
                    elif choice2 ==8 :
                        print("\n")
                        massege = input("Enter your comment: ")
                        proton.addcommentontask()
                        print("\n")
                    elif choice2 ==9 :
                        print("\n")
                        result=input("Enter your solve: ")
                        proton.solvetask(result)
                        print("\n")
                    elif choice2 ==10 :
                        print("\n")
                        proton.submittask()
                        print("\n")
                    elif choice2 ==11:
                        break
                else :
                    break
        elif choice1==2:
            instructor =Instructors(input("Enter your username: "),int(input("And age please: ")))
            print(instructor.prinformations())
            instructor.notifications1()
            instructor.notifications2()
            instructor.notificationsubmit()
            print("\n")
            while True :
                print("chosse what do u want\n 1) View Session\n 2) Add Comment\n 3) View Task\n 4) View Users\n 5) Share Session\n 6) Download Session\n 7) Add Comment on session\n 8) Add Comment on Task\n 9) Check Task\n 10) Add User\n 11) See Works\n 12) Add Finshed Tasks\n 13) See Correct Answer\n 14) Add Task \n 15)Exit")
                choice2 = int(input(">"))    
                if choice2 <16 or choice2 >0 : 
                    if choice2 ==1 :
                        print("\n")
                        instructor.viewSession()
                        print("\n")
                    elif choice2 ==2 :
                        print("\n")
                        massege = input("Enter your comment: ")
                        instructor.addcomment()
                        print("\n")
                    elif choice2 ==3:
                        print("\n")
                        instructor.viewTask(task)
                        print("\n")
                    elif choice2 ==4:
                        print("\n")
                        instructor.viewusers()
                        print("\n")
                    elif choice2 ==5:
                        print("\n")
                        instructor.shareSession()
                        print("\n")
                    elif choice2 ==6:
                        print("\n")
                        instructor.downloadSession()
                        print("\n")
                    elif choice2 ==7 :
                        print("\n")
                        massege = input("Enter your comment: ")
                        instructor.addcommentonsession()
                        print("\n")
                    elif choice2 ==8 :
                        print("\n")
                        massege = input("Enter your comment: ")
                        instructor.addcommentontask()
                        print("\n")
                    elif choice2 ==9 :
                        print("\n")
                        instructor.checktask()
                        print("\n")
                    elif choice2 ==10:
                        print("\n")
                        user= input("Enter the username of the person u want to add: ")
                        instructor.adduser(user)
                        print("\n")
                    elif choice2 ==11:
                        print("\n")
                        instructor.seeworks()
                        print("\n")
                    elif choice2 ==12 :
                        print("\n")
                        instructor.addfinshedtasks()
                        print("\n")
                    elif choice2 ==13:
                        print("\n")
                        instructor.seecorrectanswer()
                        print("\n")
                    elif choice2 ==14 :
                        print("\n")
                        instructor.addTask(task)
                        day=input("Enter a day")
                        instructor.addtimeforsubmit(day)
                        print("\n")
                    elif choice2 ==15:
                        break
                else:
                    break    
        elif choice1==3:
            exproton =Ex_Protons(input("Enter your username: "),int(input("And age please: ")))
            print(exproton.prinformations())
            exproton.notifications1()
            exproton.notifications2()
            exproton.notificationsubmit()
            while True :
                print("chosse what do u want \n 1) View Session \n 2) Add Comment \n 3) View Task \n 4) View Users \n 5) Share Session \n 6) Download Session \n 7) Add Comment on session \n 8) Add Comment on Task \n 9) Check Task \n 10) Add User \n 11) See Works \n 12)Add Finshed Tasks \n 13) See Correct Answer\n 14) Exit")
                choice2 = int(input(">"))    
                if choice2 <15 or choice2 >0:
                    if choice2 ==1 :
                        print("\n")
                        exproton.viewSession()
                        print("\n")
                    elif choice2 ==2 :
                        print("\n")
                        massege = input("Enter your comment: ")
                        exproton.addcomment()
                        print("\n")
                    elif choice2 ==3:
                        print("\n")
                        exproton.viewTask(task)
                        print("\n")
                    elif choice2 ==4:
                        print("\n")
                        exproton.viewusers(users)
                        print("\n")
                    elif choice2 ==5:
                        print("\n")
                        exproton.shareSession()
                        print("\n")
                    elif choice2 ==6:
                        print("\n")
                        exproton.downloadSession()
                        print("\n")
                    elif choice2 ==7 :
                        print("\n")
                        massege = input("Enter your comment: ")
                        exproton.addcommentonsession()
                        print("\n")
                    elif choice2 ==8 :
                        print("\n")
                        massege = input("Enter your comment: ")
                        exproton.addcommentontask()
                        print("\n")
                    elif choice2 ==9 :
                        print("\n")
                        exproton.checktask()
                        print("\n")
                    elif choice2 ==10:
                        print("\n")
                        exproton.adduser()
                        print("\n")
                    elif choice2 ==11:
                        print("\n")
                        exproton.seeworks()
                        print("\n")
                    elif choice2 ==12 :
                        exproton.addfinshedtasks()
                    elif choice2 ==13:
                        exproton.seecorrectanswer()
                    elif choice2 ==14:
                        break
                else:
                    break
    else:
        break