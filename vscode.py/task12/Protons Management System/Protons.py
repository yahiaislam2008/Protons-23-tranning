from system import system
class Protons(system) :
    def __init__(self , name , age ):
        self.name = name
        self.age =age 
        system.__init__(self ,name,age)
    def solvetask(self ,result):
        return(result)
    def submittask(self):
        print("Your task has been delivered")
    def timeforsubmit(self ,day):
        print("U have until",day)