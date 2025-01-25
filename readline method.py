# readline() method read single line from the file. if we want to read multiple lines , we can use the loop
f = open('file1.txt' , 'r')
while True:
  line =f.readline()
  if not line:
    break
  print(line) 

f = open('readline1.txt' ,'r')
i =0
while True:
  i+=1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student{i} in maths is: {m1}")
  print(f"Marks of student{i} in Sst is :{m2}")
  print(f"Marks of student{i} in English is:{m3}")
  print(line)
  