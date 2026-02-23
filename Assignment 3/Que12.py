# Q12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    first_digit = num // 100
    last_digit = num % 10

    if first_digit == last_digit:
        print("The number is a Palindrome.")
    else:
        print("The number is NOT a Palindrome.")
else:
    print("Please enter a valid 3-digit number.")