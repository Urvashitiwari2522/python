'''map(), filter() , and reduce() function are built in functions that allow you to apply a function to a sequence of 
the elements and return a new sequence'''
# MAP
def cube(x):
    return x*x*x 

lists = [1,2,3,4,5,6,7,8,9,10]
result = list(map(cube,lists))
print(result)


list1=[2,3,4,5,6,7]
result = list(map(lambda i:i*i*i,list1))
print(result)