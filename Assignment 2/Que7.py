# Q.7  Find the sum of three-digit number.
# Take input
num=int(input("Enter a three-digit number:"))
#Calculate sum of digits
digit1=num//100
digit2=(num%100)//10
digit3=num%10
sum_of_digits=digit1+digit2+digit3
print(f"Sum of digits of {num} is {sum_of_digits}.")