class system :
    def __init__(self , name ,age):
        self.name = name
        self.age =age        
    def prinformations(self):
        print("Hello",self.name)
    def viewSession(self):
        print("her is the link of materal just go and see it 'https://classroom.google.com/c/NjE2MTE4MTcwNzI4/m/NjE5MDQ2MDMxMDkx/details'")
    def notifications1(self):
        print("there is a new material")
    def notifications2(self):
        print("there is a new task")
    def addcomment(self):
        print("your comment has been add")
    def viewTask(self ,task):
        print(task)
    def viewusers(self,users):
        for i in range(len(users)):
            print(users[i])
    def shareSession(self):
        print("her is your link to share it 'https://classroom.google.com/c/NjE2MTE4MTcwNzI4/m/NjE5MDQ2MDMxMDkx/details'")
    def downloadSession(self):
        print("Download is complete")
    def addcommentonsession(self ):
        print("your comment has been add")
    def addcommentontask(self):
        print("your comment has been add")