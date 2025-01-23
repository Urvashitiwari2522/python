# seek and tell() function are used to work with file object and their positions within a file
# These function are the part of the built in io module
'''seek() => The seek() function allow you to move the current position within a file to a specific point
The position is specified in a byte , you can move either forword or backword from the current position '''
with open('file1.txt' , 'r') as f:
# move to the 10th byte in the file
  f.seek(10)
# read the next 5 byte
  data = f.read(7) 
  print(data)
#   tell() function => The tell function return the current position within the file, in bytes , These can be usedfull for 
# keeping track  of your location withiin the file 
with open('file1.txt' , 'r') as f:
#  data = f.read(12)
 current_popsition= f.tell()
 f.seek(current_popsition)