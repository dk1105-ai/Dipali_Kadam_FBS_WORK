# Q.3 . Write a program to reverse a given number using recursive function.
def reverse(n):
    rev = 0
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10
    return rev

def rev(n):
    return reverse(n)

n = int(input("Enter number: "))
result = rev(n)
print(f"The reverse of the number is: {result}")
