# 9.Write a program to calculate the m to the power n using recursion.
def power(m,n):
    if n==0:
        return 1
    else: 
        return m**n
def calculate_power(m,n):
    return power(m,n)
m=int(input("Enter the value of m:"))
n=int(input("Enter the value of n:"))
print(f"{m} to the power {n} is: {calculate_power(m,n)}")
