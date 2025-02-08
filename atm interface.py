
'''Atm interface program'''
pin_code = 9191
total_Amount = 1000000
pin= int(input("Enter your pincode:"))
if(pin!=pin_code):
   print("Your pin is incorrect[Try Again!]")
else:
  print("Your pin is correct")
  print("Welcome to State Bank Of India")
  print("Automated Teller Machine")
  print("Please enter 1 for Deposit Money!")
  print("Please enter 2 for Withdraw Money!")
  print("Please enter 3 for Check Balance!")
  print("Please enter 4 for Exit")
  while True:
   x = int(input("Select any one:"))
   if(x==1):
     deposit = int(input("Enter money to be deposited:"))
     total_Amount = total_Amount + deposit
     print("Succesfully deposited!")
     print("Total amount is:",total_Amount)
   elif(x==2):
     withdraw = int(input("Enter the withdraw money:"))
     if(total_Amount>=withdraw):
      total_Amount = total_Amount - withdraw
      print("Total money is:",total_Amount)
     else:
      print("Insufficiant Balance")
  
   elif(x==3):
     print("Total balance is:",total_Amount)
 
   elif(x==4):
     print("Exit:")
 
   else:
     print("Error")
     print("Please enter valid input!")
  