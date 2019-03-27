class Company:

  def __init__(self, place):
    self.place = place
  def display(self):
    print ('Place = ',self.place)

class Employee(Company):

   def __init__(self, place, name):
     Company.__init__(self, place)
     self.name = name

   def disp_name(self):
     print ('Name = ',self.name)

obj = Employee('chennai','jack')
obj.disp_name()
obj.display()