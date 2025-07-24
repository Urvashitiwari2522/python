class Student:
    def Student_name():
        while True:
            name=input("Enter your name:")
            if name.isalpha():
               return name
            else:
               print("Invalid input,Please enter valid name usiing alphabet:")
    def Student_age():
        while True:
            age=input("Enter your age:")
            if age.isdigit() and int(age)>0:
               return age
            else:
               print("Enter valid age number:")
s1=Student
name = s1.Student_name()
age= s1.Student_age()
print(f"hello, {name}! you are {age} years old")
