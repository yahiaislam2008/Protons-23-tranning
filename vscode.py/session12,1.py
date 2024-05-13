class show :
    def __init__(self,showname,gener,actors):
        self.actors =actors
        self.showname = showname
        self.gener =gener

    def shownameee(self):
        print(self.showname)

    def showcast(self):
        for i in range(1,len(self.actors)+1):
        
            print(i,")",self.actors[i-1])
    def addactor(self , actor):
        self.actors.append(actor)
        
    def castnumber(self):
        print(len(self.actors))

    
show1 = show("THE BIG","comedy",["Jonney","7zlqom"])

show1 .shownameee()
show1 .showcast()
show1 .addactor(input("Enter actor to add: "))
show1 .showcast()
show1 .castnumber()