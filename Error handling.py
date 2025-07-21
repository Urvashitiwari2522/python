# Excception handling is the process of responding to unwanted or unexpected event when a computer program runs.
#  Exception handling deals with these events to avoid the program or system crashing, and without this process,
# exception would disrupt the normal operation of a program.
# Python try ...except

a = input("Enter the number:")
print(f"multiplication table of {a} is:") 
# try...except blocks are used in python to handle error and exceptions. The code in try blocks runs when there is no error .
# if the try blocks catches the error, then the except block is executed 
try:
    for i in range(1,11):
      print(f"{int(a)}*{i} = {int(a)*i}")
except Exception as e:
    # print(e)
    print("Sorry some error occurred" )
print("end of program!")