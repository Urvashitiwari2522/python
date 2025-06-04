# List(mutable)
my_list = [12,23,17,54,42]
my_list.append(23)
print("updated list:",my_list)

# Dictionary(Mutable)
my_dicts={"name":"Urvashi","age":18}
my_dicts["age"]=20
print("update dict:",my_dicts)

# Tuple(immutable)
my_tup = (2,3,4,5,6)
# my_tup[0]=12 #this line gives an error
print("tuple:",my_tup)

# function
def my_function(x,y):
    return x+y
result = my_function(2,6)
print("The sum of two number is:",result)

# recursive function for factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
factorial(5)
print("factorial of the given number is:",factorial(5))

# recursive function for fibonacci
def fibonacci(x):
    if x<=0:
        return "Invalid Input"
    elif x==1:
        return 0
    elif x==2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)#Recursive call
for i in range(1,11):
    # Print firsst 10 fibonacci num
    print(fibonacci(i),end=" ")
    

