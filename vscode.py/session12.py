class car:
    def  __init__(self,color ,model,speed) :
        self.color = color
        #self.color = "red"
        self.model =model
        self.speed = speed
        #self for not car
    
    def showmodel(self):
        print(self.model)
 
    def showspeed(self):
        print(self.speed)

    def addone(self,x):
        return x +1

colorrr =input ("Enter color: ")
car1 = car (colorrr , "X7" ,"11111")
car2 = car ("green" , "X4" ,"11")
print (car2 .color)
print (car1.model)
car1 .showmodel()
car1 .showspeed()
print(car1.addone(9))