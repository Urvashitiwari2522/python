x=int(input("Enter the number of elements in tuple:"))
user_list=[]
for i in range(x):
    num=int(input("Enter the element:"))
    user_list.append(num)
    tuple(user_list)
print("tuple is:", user_list)
x1=int(input("Enter the number of elements in tuple2:"))
user_list1=[]
for i in range(x1):
    num1=int(input("Enter the element:"))
    user_list.append(num1)
    tuple(user_list1)
print("Second tuple is:",user_list)
print("press 1 to find greatest elements:")
print("press 2 to check superset:")
print("press 3 to check subset:")
x3=int(input("Choose any one option 1/2/3:"))
if(x3==1):
    for i in user_list:
        max = user_list[i]
        if(user_list[i]>user_list[i+1]):
            max=user_list[i+1]
            print("max elements is:",max)
if(x3==2):
    user_list.issubset(user_list1)
if(x3==3):
    user_list1.issuperset(user_list1)
