from system import system
from mangsystem import mangsystem
class Instructors(system,mangsystem) :
    def __init__(self , name , age):
        self.name=name
        self.age =age
        system.__init__(self,name,age ,self.users)
        mangsystem.__init__(self , name)
    #def prinformations(self):
     #   print("Hello",self.name,"your agr is",self.age)
  #  def checktask(self):
   #     print("3ash🔥🔥")
    #def viewSession():
    #    print("Debuging is so great anfd it will help u alot at your programming life")
    def addTask(self , task):
        print(task ,"rbna m3ak🤚✋")
    def addtimeforsubmit(self ,day):
        print("The day for submit is ",day)
    #def notifications1(massege):
     #   print("U have new material")
    #def notifications2(massege):
     #   print("U have a new task")
   # def notificationsubmit(self):
    #    print("there is a project has been deliverd")
    #def addcomment(massege):
     #   print(massege)
    #def viewTask(task):
     #   print(task)
    #def viewusers(users):
  #   #   print(users)
   # def adduser(self,user):
    #    self.users.append(user)
    #def shareSession():
     #   print("her is your link to share it 'https://classroom.google.com/c/NjE2MTE4MTcwNzI4/m/NjE5MDQ2MDMxMDkx/details'")
    #def downloadSession():
     #   print("Download is complete")
   # def seeworks(self):
    #    print("turtle\ntrianle\nmovies\ngit")
   # def addfinshedtasks(self,tasks):
    #    tasks=input("Enter finished tasks and spreed them by comma: ").split(",")
     #   for i in range(len(tasks)):
      #    print(tasks[i])
   # def seecorrectanswer(self):
    #    print("https://github.com/yahiaislam2008/Protons23_Session11-team6-")