class mangsystem:
    def __init__(self , name):
        self.name = name
    def checktask(self):
        print("3ash🔥🔥")    
    def notificationsubmit(self):
        print("there is a project has been deliverd")
    def adduser(self,user,users):
        users.append(user)    
    def seeworks(self):
        print("turtle\ntrianle\nmovies\ngit")
    def addfinshedtasks(self,fntasks):
        tasks=input("Enter finished tasks and spreed them by comma: ").split(",")
        for i in range(len(tasks)):
            print(tasks[i])
            fntasks.append(tasks[i])
    def showingfntasks(self , fntasks):
        for i in range(len(fntasks)):
            print(fntasks[i])
    def seecorrectanswer(self):
        print("https://github.com/yahiaislam2008/Protons23_Session11-team6-")