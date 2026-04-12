# Q.2 . Write a program to check if given number is Armstrong or not using recursive function.
def sum(n):
    if n == 0:
        return 0
    else:
        digit = n % 10
        return (digit ** 3) + sum(n // 10)
def sof(n):
   return sum(n)
n=int(input("Enter number:"))
result=sof(n)
if result == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
