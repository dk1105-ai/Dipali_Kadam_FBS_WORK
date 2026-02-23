# Q4.Write a program to input all sides of a triangle and check whether triangle is valid or not .
side1=float(input("Enter side 1:"))
side2=float(input("Enter side 2:"))     
side3=float(input("Enter side 3:"))
if (side1>0 and side2>0 and side3>0 and (side1+side2)>side3 and (side2+side3)>side1 and (side1+side3)>side2):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")