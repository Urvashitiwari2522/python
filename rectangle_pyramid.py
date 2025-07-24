'''
********
********
********
'''
row=int(input("Enter the number for row:"))
column=int(input("Enter the number for column:"))
for i in range(1,row+1):
    for j in range(1,column+1):
        print("*",end="")
    print()