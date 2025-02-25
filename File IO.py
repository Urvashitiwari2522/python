'''Opening a file => Before we can perform any operations on the file, we must first open it
 python provide a open() function to open a file
 open the file'''
'''Modes in file =>There are various modes in which we can open a file
read(r),write(w),append(a),create(x),text(t),binary(b) '''
f = open('file.txt','r')
print(f)
# read the file
text = f.read()
print(text)
# Closing a file => it is important to close the file after you are done with it.
f.close()
# write the file
f = open('file.txt','w')
f.write('Hello')
# Append te file
f = open('file.txt','a')
f.write("Hello, world")
f.write("Hello, world")
f.close() 
'''The with statement => Alternatively, you can used the with statement to automatically close the file after 
you are done with it.'''
with open('file.txt','a') as f:
    f.write("hii")
with open('file1.txt','w') as f:
    f.write("Hey, I am Urvashi!")
with open('readline.txt','w') as f:
    f.write("43,87,98\n")
    f.write("87,67,79\n")
    f.write("98,90,95")
