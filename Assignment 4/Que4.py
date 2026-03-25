# Q4. WAP to print factorial of a number .
n=int(input("enter no:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"factorial of {n} is {fact}.")