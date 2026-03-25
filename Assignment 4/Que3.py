# Q3. WAP to print sum of series upto n.
n=int(input("enter no:"))
sum=0       
for i in range(1,n+1):
    sum=sum+i
print(f"sum of series upto {n} is {sum}.")