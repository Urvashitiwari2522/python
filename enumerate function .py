# Enumerate function in python->The enumerate function in built-in-function in python that allows you to 
# loop over a sequence(such as list,tuple,and string) and get the index and value of each element in the sequence at the same time

'''
index=0
price=[23,56,787,433,234,543]
for price in prices:
    print(price)
    if (index==3):
        print("hello)
    index=+1'''


# by enumerate function
marks=[56,78,98,90,100,93]
for index,mark  in enumerate(marks):
    print(mark)
    if index==4:
        print("Full mark")