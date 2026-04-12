# Q.1 Write a program to find sum of following series using recursive functions: 1! + 2!  + 3! + 4! +….. + n!  

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
def sum_of_series(n):
    if n==1:
        return 1
    else:
        return fact(n)+sum_of_series(n-1)
    
n=int(input("Enter number:"))
result=sum_of_series(n)
print(f"The sum of the series is: {result}")