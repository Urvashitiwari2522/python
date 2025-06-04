''' The os module in python is a built-in library that provide function for interacting with operating system
 it provides you to perform a wide variety of tasks, such as opening, reading and writting files, interacting with the file system,
  and running system command '''
import os
if (not os.path.exists("data")):
  os.mkdir("data")
for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")
    # os.rename(f"data/Day{i+1}" , f"data/File{i+1}")

folders = os.listdir("data")               
print(folders)