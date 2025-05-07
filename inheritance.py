class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def show_Details(self):
        print(f"The name of emplyee:{self.id} is {self.name}")
        # Inheritance->When a class derive in another class
class Programmer(Employee):
    def Show_language(self):
        print("The defualt language is python:")
emp=Employee("420","Rohan")
emp.show_Details()
e1=Programmer("200","Urvashi")
e1.show_Details()
e1.Show_language()