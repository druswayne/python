import math, cmath
try:
    a=float(input("a"))
    b=float(input("b"))
    c=float(input("c"))
    D=b**2-4*a*c
    if D>0:
        x_1=(-b-math.sqrt(D))/(2*a)
        x_2=(-b-math.sqrt(D))/(2*a)
        print(x_1,x_2)
    elif D==0:
        x_0=(-b)/(2*a)
        print(x_0)
    else:
        x_1 = (-b - cmath.sqrt(D)) / (2 * a)
        x_2 = (-b - cmath.sqrt(D)) / (2 * a)
        print(x_1, x_2)
except:
    print("error")