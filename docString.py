# python doctring are the string literal that appear right after the defination of a function,method,class, or module
def square(n):
    '''Takes in a number n, return the square of n'''
    print("Square of number n:",n**2)
    # print("Cube of number n:",n**3)
square(5)
print(square.__doc__)


