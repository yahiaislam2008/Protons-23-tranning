from system import system
class Protons(system) :
    def __init__(self , name , age ):
        self.name = name
        self.age =age 
        system.__init__(self ,name,age)
    #def prinformations(self):
    #    print("Hello",self.name,"your agr is",self.age)
    def solvetask(self ,result):
        return(result)
    def submittask(self):
        print("Your task has been delivered")
    #def viewSession():
     #   print("her is the link of materal just go and see it 'https://classroom.google.com/c/NjE2MTE4MTcwNzI4/m/NjE5MDQ2MDMxMDkx/details'")
    def timeforsubmit(self ,day):
        print("U have until",day)
    #def notifications1(massege):
     #  print("U have new material")
    #def notifications2(massege):
     #   print("U have a new task")
    #def addcomment(massege):
     #   print(massege)
    #def viewTask(task):
     #   print(task)
    #def viewusers():
     #   print("Yahia Islam","Farris","Abdallah Elsherbiny","yousef saeed")
    #def shareSession():
     #   print("her is your link to share it 'https://classroom.google.com/c/NjE2MTE4MTcwNzI4/m/NjE5MDQ2MDMxMDkx/details'")
    #def downloadSession():
     #   print("Download is complete")