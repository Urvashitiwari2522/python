# Global 
# A variable is a named location memory that stores a value or data
# Local variable -> A local variable is a variable that is defined inside the function and  is only accessible within a function
# Global variable -> A global variable is a variable that is define outside the function and is accessible from within 
# any function of your code
x = 5
print("X is global variable:",x)
# Local variable
def hello():
    x = 10
    print("Hello Urvashi")
    print("X is local variable",x)

# function call 
hello()
# print local variable
print(x)
