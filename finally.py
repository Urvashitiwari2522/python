# finally code block is also a part of exception handling. When we handle exception using the try and except block
# , we can include a finally block at the end. The finally block is always executed
num1 = int(input("Enter the number:"))
num2 =int(input("Enter the second number:"))
try:
    if num2 == 0:

        print("second number is zero!")
    else:
        print(num1/num2)
except Exception as e:
   print(e)
finally:
    print("Finally block is executed>>>")
    print("I am always executed")