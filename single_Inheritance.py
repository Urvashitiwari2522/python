class Person:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Person Initialised:\n","name:",self.name)
class Student(Person):
    def __init__(self,name,roll):
        self.roll=roll
        super().__init__(name) #Call Parent's constructor
    def Display(self):
        self.show()
        print("Student Initialised:\n","roll:",self.roll)
obj=Student("Pri",101)
obj.Display()