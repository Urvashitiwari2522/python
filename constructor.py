# constructor-> A constructor is a special method in the class used to create and initilize  an object of the class. There are different
#  type of constructors. Constructor is invoked automatically when an object of the class is created.
class Person:
    def __init__(self,name,occupation):
       # init is a one of the reserved function in python
      self.name=name
      self.occ=occupation

    def info(self):
      print(f"{self.name} is a {self.occ}")

a=Person("priya","programmer")
b=Person("harry","full stack")
a.info()
b.info()
