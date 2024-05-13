from system import system
from mangsystem import mangsystem
class Ex_Protons(system,mangsystem) :
    def __init__(self , name ,age):
        self.name = name
        self.age =age
        system.__init__(self,name,age)
        mangsystem.__init__(self , name)