#Write a python program to convert a message into secret code language. 
# import random 

print("write 'code' for coding:")
print("write 'decode' for decoding:")
st=input("Enter choice:")

if(st=="code"):
   mess=input("Write a message:")
   words = mess.split()
   code=[]
   for i in words:
     if(len(st)<=3):
       words=(i[1:])+i[0]
       code.append(words)
     else:
      first=i[0]
      second=i[1:]
      last=i[len(i)-1]
      words=(i[1:])+i[0]
      new_word=first+last+second+words+last+second+first
      code.append(new_word)
   scode=""
   print((scode.join(code)))
else:
   mess1=input("Write a message:")
   words = st.split()
   code=[]
   for i in words:
    if(len(st)<=3):
       words=(i[1:])+i[0]
       code.append(words)
    else:
      new_word=words[3:-3]
      new_word=new_word[-1]+new_word[::-1]
      code.append(words)
    print((code))
