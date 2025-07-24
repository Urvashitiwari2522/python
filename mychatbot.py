def personal_chatbot():
    print("Hello i am your personal chatbot.type bye to exit!")
    while True:
       user_input = input("you:").lower()
       if user_input=="bye":
         print("chatbot: Goodbye! Have a nice day.")
         break
       elif "hello" in user_input or "hi" in user_input:
          print("chatbot: Hello sweetheart!")
       elif "who are you" in user_input:
          print("chatbot: I am your life partner!")
       elif "your name" in user_input:
          print("chatbot: priya")
       elif "how are you" in user_input:
          print("if you are fine then i am too good.")
       elif "how much do you love me" in user_input:
          print("chatbot: error! memory stack overflow.")
       elif "wha" in user_input:
          print("chatbot:i love you")
       else:
          print("chatbot: i am always with you.")
    # run
personal_chatbot()