# Q.7 Write a program to find sum of digits of a number. 
def sof(n):
    sum=0
    while n > 0:
        if n == 0:
            return 0
        else:

            d=n%10
            print(d)
            sum+=d
            n=n//10
    return sum

    # return d+sof(n//10)
n=int(input("Enter number:"))
print(f"Sum of digits: {sof(n)}")
