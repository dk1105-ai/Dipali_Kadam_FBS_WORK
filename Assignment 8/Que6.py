# Q.6  Write a program to find print the following Fibonacci series using functions: 1  1  2  3 5 8  n terms 
def fibonacci(n):
    a=-1
    b=1
    for i in range(n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
n=int(input("Enter the number of terms:"))
fibonacci(n)
# print(f"The Fibonacci series up to {n} terms is: {res}")