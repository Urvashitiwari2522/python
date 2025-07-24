user_input=int(input("Enter the numbers of elements in the tuple:"))
user_list=[]
i=0
while(i<user_input):
    x=int(input("Enter element:"))
    user_list.append(x)
    y=x**3
    list=[x,y]
    print("Elements and their cuube:",list)
    i=+1

