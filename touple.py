# tuple are ordered collection of items.They store multiple items in single variable(tuple are immutable)
tup1 = (2,4,3,12,45,65,4,3,2)
print(tup1)
print(type(tup1))
tup =("red","green","pink","yellow")
print(tup)
tup2 =tup[:2]
print(tup2)
# methods of tuple

# tuple are immutable, hence if you want to add,remove and change tuple items, then first you must convert the tuple to the list.
countries = ("India","Italy","England","Germany")
print(countries)
temp = list(countries)
temp.append("Russian") #add item
temp.pop(3)            #remove item
temp[2] = "finland"    #change item
print(temp)
countries =tuple(temp)
print(countries)

# concatenate two tuple
countries2 =("Russian","china","Pakistan")
add = countries+countries2
print(add)

# count() method is used to count the number of item
result = tup1.count(2)
print("Count of 2 in tup1 :",result)

# index() method returns the first occurrence of the given element of the tuple
res =tup1.index(4)
print("First occurence of 3 :",res)