class ManagementSystem:
    def __init__(self, role):
        self.role = role

    def view_session(self):
        print("Viewing session")

    def add_task(self):
        print("Adding task")

class Instructor(ManagementSystem):
    def __init__(self):
        super().__init__("Instructor")

    def check_task(self):
        print("Checking task")

class ExProton(ManagementSystem):
    def __init__(self):
        super().__init__("ExProton")

    def check_task(self):
        print("Checking task")

class Proton(ManagementSystem):
    def __init__(self):
        super().__init__("Proton")

    def solve_tasks(self):
        print("Solving tasks")

# Create instances of each role
instructor = Instructor()
ex_proton = ExProton()
proton = Proton()

# Access functionalities based on role
instructor.view_session()
instructor.add_task()
instructor.check_task()

ex_proton.view_session()
ex_proton.add_task()
ex_proton.check_task()

proton.view_session()
proton.add_task()
proton.solve_tasks()