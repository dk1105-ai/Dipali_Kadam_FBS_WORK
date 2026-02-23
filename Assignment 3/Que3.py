# Q3. Write a program to input angles of a triangle and check whether triangle is valid or not.
ang1=int(input("Enter angle 1:"))
ang2=int(input("Enter angle 2:"))
ang3=int(input("Enter angle 3:"))
total=ang1+ang2+ang3
 
if(total==180 and ang1>0 and ang2>0 and ang3>0):
        print("The triangle is valid.")
else:
        print("The triangle is not valid.")