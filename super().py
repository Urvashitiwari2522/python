class Employee_name:
    def __init__(self,Emp_name):
        self.Emp_name = Emp_name
        print("Employee name is:",Emp_name)
class Employee_salary(Employee_name): #Inherite super class
    def __init__(self,Emp_name,Emp_salary):
        self.Emp_salary=Emp_salary
        super().__init__(Emp_name) #Call Parent's constructor
        print("Salary:",Emp_salary)
obj = Employee_salary("Priyankar",100000)

