a,b,c=int(input("enter coeff of x^2")),int(input("enter coeff of x")),int(input("enter constant"))
d=(b*b)-(4*a*c)
if d==0:
    print("REAL AND EQUAL ROOTS")
elif d>0:
    print("REAL AND DISTINCT ROOTS")
elif d<0:
    print("IMAGINARY ROOTS")
z=(-b+(d**0.5))/(2*a)
y=(-b-(d**0.5))/(2*a)
print("the root of the equation is ",z)
print("the root of the equation is ",y)
