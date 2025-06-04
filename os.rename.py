import os
for i in range(0,100):
    # os.mkdir(f"data/Day{i+1}")
    os.rename(f"data/Day{i+1}" , f"data/File{i+1}")
folders = os.listdir("data")               
print(folders)
 