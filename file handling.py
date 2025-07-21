lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
 
with open("example1.txt", "w") as file:
    #  Writes a single string to the file
    file.write("Hello, world!\n")
    file.write("Welcome to Python file handling\n")
    # `writelines()` Method
    file.writelines(lines)
    print("This is printed to a file.", file=file)
# write()
with open("w_demo.txt", "w") as f:
    f.write("Write method\n")
 # writelines()
with open("wl_demo.txt", "w") as f:
    f.writelines(["One\n", "Two\n", "Three\n"])
 # print()
with open("p_demo.txt", "w") as f:
 print("Printed line 1", file=f)
 print("Printed line 2", file=f)