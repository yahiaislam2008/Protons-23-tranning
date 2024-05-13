from persons import persons
class database(persons):
    def __init__(self,database):
        super().__init__()
        self.database=database
        self.database = {}
    def sortbyname(self):
        