x=int(input("Enter the number of elements in the tuple:"))
user_list=[]
for i in range(x):
    x1=int(input("Enter the element:"))
    user_list.append(x1)
    tuple(user_list)
print("Tuple:",user_list)
list=[]
list2=[]
for i in range(x):
    y=((user_list[i])%2==0)
    list.append(y)
    z=list.count(y)
    y1=((user_list[i])%2!=0)
    list2.append(y1)
    z1=list2.count(y1)
print("total even number is:",z)
print("total odd number is:",z1)
   

