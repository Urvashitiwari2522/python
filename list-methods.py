lists =[1,1,3,2,10,4,5,7,8,9]
print(lists[:])

# append() method is used to append
lists.append(11)
print("Apppend:",lists)

# sort() method is used to sort the given list in ascending order
lists.sort()
print("Increasing order:",lists)

#reverse() method is used to sort the given list in descending order 
lists.reverse()
print("Decreasing order:",lists)

# index() method return the first occurances of the list
print("At index(1):",lists.index(1))

# count() method return the count of the no of item in the given list item.
lists.count(1)
print("count of 1:",lists.count(1))

# copy() method returns the copy of the list
l2 = lists.copy()
print("copy list l2 is:",l2)

# insert() method used to insert item atgiven index
color = ["green" , "pink" , "red" , "yellow" , "white"]
color.insert(1,"blue")
print("original color:",color)
print("insert blue color at index 1:",color)

#  concatenate() method can simply concatenate two list to join two lists.
veg =["cabbage" , "radish" , "tomato" , "potato" , "garlic"]
print("concatenating color and veg:",color+veg)

# extends() is used to adds an entire list with existing list.
color.extend(veg)
print("Extend veg to color:",color)
