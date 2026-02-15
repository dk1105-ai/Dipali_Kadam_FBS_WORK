# Q.7  Program to Find the Roots of a Quadratic Equation

import math
# take input
a=int(input("Enter coefficient of x^2:"))
b=int(input("Enter coefficient of x:"))
c=int(input("Enter constant term:"))    
# calculate discriminant
D=b**2-4*a*c
# calculate roots
if D>0:
    root1=(-b+math.sqrt(D))/(2*a)
    root2=(-b-math.sqrt(D))/(2*a)
    print(f'Two distinct real roots are {root1} and {root2}.')      

elif D==0:
    root=-b/(2*a)
    print(f'Two equal real roots are {root} and {root}.')
else:
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(-D)/(2*a)
    print(f'Two complex roots are {real_part}+{imaginary_part}j and {real_part}-{imaginary_part}j.')

    