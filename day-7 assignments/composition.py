class Student:
    def __init__(self, departmentname):
        self.eg = departmentname

    def total(self):
        print("The total number of student is 1000")


class College:
    def __init__(self, name, Student):
        self.name = name
        self.student1 = Student

    def display(self):
        print(self.student1.total())


mystudent = Student('ece')
mycollege = College('peri', mystudent)
mycollege.display()


