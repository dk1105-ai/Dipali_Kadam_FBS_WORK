# Q8. Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random
userid=input("Enter userid:")
password=input("Enter password:")
if(userid=="dipali" and password=="dipali123"):
    print("Login successful.")
    random_num=random.randint(1000,9999)
    print("Captcha:",random_num)
    user_input=int(input("Enter the captcha:"))
    if(user_input==random_num):
        print("Captcha verification successful.")
    else:
        print("Captcha verification failed.")