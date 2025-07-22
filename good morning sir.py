import time
t =time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)
minut = int(time.strftime('%M'))
print(minut)
second = int(time.strftime('%S'))
print(second)
if(hour>=24 and hour<12):
    print("Good morning sir !")
elif(hour>=12 and hour<17):
    print("Good Afternoon !")
if(hour>=17 and hour<24):
     print("Good Night !")    
