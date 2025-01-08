# factorial(0)==1
# factorial(1)==1
# factorial(num) = num*factorial(num-1)
def factorial_calculation(num):
   if(num==0 or num==1):
    return 1
   else:
     return num * factorial_calculation(num-1)
print(factorial_calculation(5))
print(factorial_calculation(10))