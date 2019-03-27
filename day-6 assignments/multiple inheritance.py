class Manager:
    def __init__(self,managerName,managerAge):
        self.name = managerName
        self.age = managerAge

    def display(self):
        print(self.name)

    def show(self):
        print(self.age)


class Employee:
    def __init__(self,employeesalary):
        self.employeesalary = employeesalary


    def getsalary(self):
        return self.employeesalary


class Factory(Manager,Employee) :
    def __init__(self,name,age,employeesalary):
        Manager. __init__(self,name,age)
        Employee.__init__(self,employeesalary)


factory1 = Factory('Jack', 32 ,'30000')
factory1.display()
factory1.show()
print(factory1.getsalary())