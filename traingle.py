'''   *
     * *
    *   *
   *     *
  * * * * *   
'''
row=int(input("Enter the number of row:"))
# column=int(input("Enter the number of column:"))
for i in range(row):
    for j in range(row-i):
         print(" ",end="")
    for j in range(2*i+1):     
         if j==0 or i==row-1 or j==2*i:
            print("*",end="")
         else:
            print(" ",end="")
    print() 
 