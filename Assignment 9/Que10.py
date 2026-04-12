# Q.10 Write a program to reverse a number using recursion. 
def reverse_number(num):
    rev=0
    while num>0:
        d=num%10
        rev=rev*10+d
        num=num//10
    return rev
def reverse(num):
    return reverse_number(num)
num=int(input("Enter the number:"))
print(f"The reverse of {num} is: {reverse(num)}")