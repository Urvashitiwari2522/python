# else statement execute
for i in range(6):
    print(i)
else:
    print("sorry! I am not 'i': ")

# else statement doesn't execute
for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("I am not i")

 # while loop with else statement
while i in range(6<10):
    print(i)
else:
    print("I am not i")