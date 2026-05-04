a=float(input("enter employee's salary"))
d=int(input("enter no of days employee was absent"))
if d>2:
   y=d-2
   print("total no of leave availed=",d)
   print("amount deducted= rs",y*500)
   print("FINAL SALARY AFTER DEDUCTION IS RS",a-(y*500))
elif d>=0 and d<=2:
   print("NO DEDUCTION IS APPLICABLE!!!!!")
   print("FINAL SALARY IS RS",a)
else:
   print("enter correct no of days")
