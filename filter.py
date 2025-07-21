# MAP => The map function applies a function to each element  in a sequence and return a new sequence containing 
# the transformed elements.
def cube(x):
    return x*x*x
lists = [1,2,3,4,5,6,7,8,9,10]
# newlist = list(map(cube,lists))
# print(newlist)

list1=[2,3,4,5,6,7]
result = list(map(lambda i:i*i*i,list1))
print(result)

# FILTER => filter function filter a sequence of elements based on the given predicate(a function that 
# return a boolean value).
def filter_function(a):
    return a>4
newlist2 = list(filter(filter_function , lists))
print(newlist2)