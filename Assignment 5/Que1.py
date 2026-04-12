# Q1.1. Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3 times. After that program to terminate.
userid="admin"
password="admin123"
for i in range(3):
    id=input("enter userid:")
    passw=input("enter password:")
    if(id==userid and passw==password):
        print("login successful.")
        break
    else:
        print("invalid credentials. try again.")
else:
    print("you have exceeded the maximum number of attempts. program terminated.")
