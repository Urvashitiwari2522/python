row=int(input("Enter the number of row:"))
column=int(input("Enter the number of column:"))
for i in range(0,row):
    for j in range(0,column):
      if i==0 or j==0 or  i==row-1 or j==column-1:
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print()
      