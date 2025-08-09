class Employee:
    """This is a representation of an employee."""
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with id {self.id}")

    def add_work(self, task):
        print(f"Added task {task} to employee {self.name}")
        self.tasks.append(task)

employee_1 = Employee("Raphael", "1234")
employee_2 = Employee("Angelo", "5343")
employee_1.add_work("Task 1")
print("Employee 1 Name: ", employee_1.name)
print("Employee 1 Tasks: ", employee_1.tasks)