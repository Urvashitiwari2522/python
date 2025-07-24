''''
*******
******
*****
****
***
**
*
'''
row=int(input("Enter the number of row:"))
for i in range(row+1,0,-1):
    for j in range(1,i+1):
        # print(i,end=" ")
        print(j,end="")
    print("")