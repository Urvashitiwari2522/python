list = ["Urvashi" , 20 ,"4thsem" , "BCA" ,"Topper of the class"]
print(list)
# print the element if the list in different line

for i in list:
    print(i)
    i=0
while (i<=4):
    print(list[i])
    i += 1
# print the elements of the list in reversed order using for and while loop

for i in reversed(list):
    print(i)

i =4
while(i>=0):
    print(list[i])
    i -= 1

# cube of all items in the list
def cube(x):
  return x*x*x
list = [1,2,3,4,5,6,7,8]
result = []
for item in list:
  result.append(cube(item))
print(result)