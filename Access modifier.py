# Access Modifiers/Specifiers -> Access Modifier and Access Specifier in Python programming are used to limit the 
# access of the class variable and class method outside of the class. while implementing the concepts of the class
class Employee:
    # Constructor is defined
    def __init__(self,name,language):
        # An indication of private variable(__)
        self.__name=name
        self.__language=language
    # An indication Protected method(_)
    def _show(self):
        print(f"The employee {self.__name} known {self.__language}")
emp=Employee("Abhay","Java")

# All the methods and variable in python are by default public.Any instance of 
emp._show()
# CAn't be accessed directly
# print(emp.name)
# Can be access indirectly
print(emp._Employee__name)
print(emp._Employee__language)
# Name Mangling -> Name mangling is a technique in Python used to protect class-private and super class-private attributes from being
#  accidentally overwritten  by subclasse
print(emp.__dir__())
print(emp.__class__)