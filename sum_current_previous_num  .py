# list=[1,2,3,4,5,6,7,8,9,10]
list=[]
x=int(input("Enter the number of elements in list:"))
for j in range(x):
    x1=int(input("Enter the elements:"))
    list.append(x1)
print("list of elements:",list)
i=0
while(i<len(list)):
    sum=(list[i-1])+(list[i])
    print(f"Sum of previous number",{i-1} ,"and current number",{i},":",sum)
    i+=1