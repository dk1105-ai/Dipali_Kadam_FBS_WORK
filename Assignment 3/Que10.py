# Q10.Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
gender=input("Enter gender (M/F): ")
age=int(input("Enter age: "))
if (gender.lower() in ['f','female']):
    if (age >= 18):
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage.")
else:
    if (age >= 21):
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage.")