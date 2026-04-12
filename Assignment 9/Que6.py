# Q.6 Write a program to print Fibonacci series using recursion.
def fib(n):
    a=-1
    b=1
    for i in range(n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
def fibonacci(n):
    return fib(n)
n = int(input("Enter number of terms: "))
print(f"Fibonacci series up to {n} terms:")
fibonacci(n)