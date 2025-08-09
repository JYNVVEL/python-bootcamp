class Employee:
    """This is a representation of an employee."""
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee: {self.name}\n      ID: {self.id}")

    def add_work(self, task):
        print(f"Added task {task} to employee {self.name}")
        print("-" * 1000)
        self.tasks.append(task)

class Recruiter(Employee):
    def recruit(self):
        self.add_work("recruit")

class Developer(Employee):
    def code(self):
        self.add_work("code")

class Manager(Employee):
    def manage(self):
        self.add_work("manage")

recruiter = Recruiter("John", 1234)
recruiter.recruit()

recruiter = Developer("Jason", 3213)
recruiter.code()

recruiter = Manager("Jona", 6857)
recruiter.manage()

