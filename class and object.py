# class -> class is a collection of similar type of object,A class is template or blueprint for creating an object
# object-> Object is a instance of the class used to access the properties of class
class person:
    name = "Urvashi"
    occupation = "Student"
    networth = 100
    def info(self):
        print(f"{self.name} is a {self.occupation }")
# creating an object 
x=person()
y=person()
z=person()
x.name="Suraj"
x.occupation="software developer"

y.name="Priya"
y.occupation="programmer"
x.info()
y.info()
z.info()