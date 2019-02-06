class Company:
    def __init__(self,companyName,emailid):
        self.name = companyName
        self.emailid = emailid

    def display(self):
        print(self.name)
        print(self.emailid)



class Manager(Company) :
    def __init__(self,companyName,emailid,managername,phonenumber):
        Company. __init__(self,companyName,emailid)
        self.managerName = managername
        self.phonenumber = phonenumber


    def show(self):
        print(self.managerName)
        print(self.phonenumber)


class Customers(Company):
    def __init__(self, companyName, emailid,productName):
        Company.__init__(self, companyName, emailid)
        self.productName = productName

    def disp(self):
        print(self.productName)



customer1 = Customers('Thoughtworks','thoughtworks.com','app')
    customer.display()
factory1.show()
print(factory1.getsalary())
