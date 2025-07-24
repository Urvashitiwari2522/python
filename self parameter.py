# self -> the self parameter is the reference to the  current instance of the class and
# it is used to access the variable that belongs to the class
class person:
    name = "Urvashi"
    occupation = "Student"
    networth ="100"
    def info(self):
      print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
a.name = "priya"
a.occupation = "Programmer"
b.name = "nikita"
b.occupation = "Software developer"
a.info()
b.info()