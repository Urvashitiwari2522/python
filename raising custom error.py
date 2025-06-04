# Raisiing Custom errors
# In Python, we can custom errors by using the raise keyword
a = int(input("Enter any value between 5 and 9:"))
if(a<5 or a>9):
   raise ValueError("Value should be between 5 and 9")
