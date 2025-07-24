'''
*
**
***
****
*****
******
'''
row=int(input("Enter the number of row:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        # print(i,end="")
        print("*",end="")
    print("")