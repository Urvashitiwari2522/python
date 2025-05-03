while True:
    sentence=input("Enter message:")
    words=sentence.split(" ")
    coding=input("1 for Coding or 0 for Decoding:")
    coding=True if(coding=="1")else False 
    print(coding)
    if(coding):
        new_word=[]
        for word in words:
            if(len(words)>=3):
                r1="dfg"
                r2="asf"
                new_sentence=r1+word[1:]+word[0]+r2
                new_word.append(new_sentence)
            else:
                new_word.append(word[::-1])
        print(" ".join(new_word))

    else:
        new_word=[]
        for word in words:
            if(len(word)>=3):
                new_sentence=word[3:-3]
                new_sentence=new_sentence[-1]+new_sentence[:-1]
                new_word.append(new_sentence)
            else:
                new_word.append(word[::-1])
        print(" ".join(new_word))