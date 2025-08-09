class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sleep(self):
        print("I will sleep for eight hours")

    def introduce(self):
        return f"Hello, my name is {self.first_name} {self.last_name}"

class Student(Person):
    def __init__(self, first_name, last_name, level):
        super().__init__(first_name, last_name)
        self.level = level

    def introduce(self):
        return super().introduce() + f" I'm a {self.level} student"

student = Student("John", "Cena", " 3rd year high school")
print(student.introduce())