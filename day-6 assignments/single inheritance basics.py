class Manager:
    def __init__(self,managerName,managerAge):
        self.name = managerName
        self.age = managerAge

    def display(self):
        print(self.name)

    def show(self):
        print(self.age)




class Factory(Manager) :
    def __init__(self,name,age):
        Manager. __init__(self,name,age)


factory1 = Factory('Jack', 32)
factory1.display()
factory1.show()
