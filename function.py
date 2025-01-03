 # def is a keyword for defining a function in python
def calculate_Arithmetic_operation(a,b):
    # sum -> Addition
    sum = a+b
    # sub -> Subtraction
    sub = a-b
    # mul -> Multiplication
    mul = a*b
    # div -> Division
    div = a/b
    print(" Addition of two number is:" ,sum ,"\n","Subtraction of two number is:", sub, "\n",
           "Multiplication of two number is:",mul ,"\n", "Division of two number is:",div)
    
#required arguments(pass the arguments in the correct positional order)
calculate_Arithmetic_operation(10,5) #required arguments
calculate_Arithmetic_operation(12,2) #required arguments

# average function for calculating avg of three number
def average_cal(x=1,y=2,z=3): #default arguments
    avg =(x+y+z)/3
    print("Average of three number is:",avg)

    # function call by value
average_cal(12,23,45)

# creating name function
def name(name="urvashi",fname="upendra",mname="rima"): #default arguments
    print("name is:",name,fname,mname)
name("priya")

#keyword arguments(arguments order doesn't matter)
name(fname="Upendra tiwari" , name="priya tiwari", mname="Rima tiwari")#keyword arguments

# keyword arbitrary arguments
def average_numbers(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum / len(numbers))
average_numbers(12,22,13)

def name(**name):
    print(type(name))
    print("Hello!" , name["myname"] , name["fname"] , name["mname"])

name(myname="Abhishek," , fname="Upendra," , mname="Rima")
