# Q.9 Write a program to check if entered number is a palindrome or not. 
def palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        d = n % 10
        reverse = reverse * 10 + d
        n = n // 10

    if original == reverse:
        print("The number is palindrome.")
    else:
        print("The number is not palindrome.")

n = int(input("Enter number: "))
palindrome(n)