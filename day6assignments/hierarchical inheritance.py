class Manager:
    def __init__(self,managerName,managerAge):
        self.name = managerName
        self.age = managerAge

    def display(self):
        print(self.name)

    def show(self):
        print(self.age)


class Factory(Manager,Employee) :
    def __init__(self,name,age,employeesalary):
        Manager. __init__(self,name,age)
        Employee.__init__(self,employeesalary)

    def disp_id(self):
        print( self.id)