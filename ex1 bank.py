b=float(input("enter initial account balance"))
if b<1000:
   print("MINIMUM INITIAL ACCOUNT BALANCE MUST BE GREATER THAN 1000RS!!!!")
else:
   print("---------MENU---------")
   print("1-deposit")
   print("2-withdraw")
   print("-----------------------")
   a=int(input("enter your choise"))
   t=b
   if a==1:
      d=float(input("enter amount to be deposited"))
      if d<500:
         print("YOUR MINIMUM DEPOSIT AMOUNT MUST BE 500RS!!")
      else:
         t=b+d
         print("ACCOUNT BALANCE=",t)
   elif a==2:
      w=float(input("enter amount to be withdrawn"))
      if w>=500:
         t=b-w
         if t<1000:
                print("AMOUNT CANNOT BE WITHDRAWN!!")
                print("MINIMUM BALANCE MUST BE 1000RS!!")
         else:
                print("ACCOUNT BALANCE=",t)
      else:
         print("MINIMUM 500RS MUST BE WITHDRAWN!!!")
   else:
      print("choose correct choise")