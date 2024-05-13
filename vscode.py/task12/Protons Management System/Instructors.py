from system import system
from mangsystem import mangsystem
class Instructors(system,mangsystem) :
    def __init__(self , name , age):
        self.name=name
        self.age =age
        system.__init__(self,name,age)
        mangsystem.__init__(self , name)
    def addTask(self , task):
        print(task ,"rbna m3ak🤚✋")
    def addtimeforsubmit(self ,day):
        print("The day for submit is ",day)