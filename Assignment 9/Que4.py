# Q.4  Write a program to find sum of n numbers using recursion.
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
def sof(n):
   return sum(n)
n=int(input("Enter number:"))
result=sof(n)
print(f"The sum of the first {n} numbers is: {result}")