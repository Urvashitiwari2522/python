# create list of tuple and print elements with their square and cube
user_input=int(input("Enter the numbers of elements in the tuple:"))
user_list=[]
user_list1=[]
for i in range(user_input):
    x=int(input("Enter element:"))
    user_list.append(x)
    y=x**3 
    z=x**2
    list=[x,z,y]
    tup=tuple(list)
    user_list1.append(tup)
print("Elements with their square and cube:",user_list1)