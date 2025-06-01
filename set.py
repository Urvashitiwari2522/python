# sets are unordered collection of items. They store multiple items in one variable. Set item are seperated by commas and enclosed with
#  curly brackets{},set are immutable  
info = {"Carla",19,False,5.9,19}
print(info)

#you can access item of set using a for loop 
for char in info:
    print(char)

# check type
harry = set()
print(type(harry))

# methods of set
s1 ={1,2,4,6,7}
s2 ={3,5,6,7}
# union() or update() method  print all items that are present in two sets
print(s1.union(s2))
(s1.update(s2))
print(s1,s2)

# intersection() and intersection_update() method print only items that are similar to both the set 
print(s1.intersection(s2))

# symmetric_difference() and symmetric_difference_update() method print only items that are not similar to both set
cities1 ={"Tokyo","Madrid","Berlin","Delhi","Seule","Kabul"}
cities2 ={"Tokyo","Seule","Kabul","Delhi"}
cities = cities1.symmetric_difference(cities2)
print(cities)

# The difference() and difference_update()methods print only item that are only  present only original set and not in both set 

# The isdisjoint() method checks if item of given set are present in anathor set.This method return false if item are present, else return True 
print(cities1.isdisjoint(cities2))

# issuperset() method checks if all the items of particular set are present in the original set
print(cities1.issuperset(cities2))

# issubset method() checks if all the items of original set are present in the particular set. It return True if all the items
#  are present,else return False
print(cities2.issubset(cities1))

# add() if you want to add a single item to the set 
cities1.add("Helsinki")
print(cities1)

# update() mthod if you want to add more than one item 
cities1.update(cities2)
print(cities1)

# remove() and discard() method used to remove item from list
cities1.remove("Helsinki")
cities1.discard("Helsinki")
print(cities1)

# pop() method remove the last element of the set
item = cities1.pop()
print(cities1)
print(item)

# del is not a method, it is a keyword that is used to delete the entire set 
del cities
# print(cities)
# output is NameError

# clear() method clear all the items of the set and print an empty set
cities1.clear()
print(cities1)