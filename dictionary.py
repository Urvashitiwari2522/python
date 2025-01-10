
# dictionaries are ordered collection of data items. They store multiple data item in single variable '{}' .
info ={'name': "Karan" , ' Age':19 , 'eligible':True }
print(info)
print(info['name'])
print(info.get('eligible'))
dic ={
    "Harry": "Human being",
    "Spoon": "Object"
}
print(dic["Harry"])
print(dic["Spoon"])
emp1 = {1:21,2:23,4:45}
emp2 = {9:34,5:66}
# update() method update the value of the key provided to it if the item already exist already  in the dictionary
emp1.update(emp2)
print(emp1)
# clear() method remove all the items of the list
emp1.clear()
print("empty dic:",emp1)
# pop() method remove the last key-value pair from the dictionary
emp2.pop(9)
print(emp2)
# del() method is used to remove a dictionary item
info = {"name":"Urvashi","age":19}
del info["age"]
print(info)
