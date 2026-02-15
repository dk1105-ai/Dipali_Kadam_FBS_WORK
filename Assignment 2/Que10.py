# Q.10 Write a program to reverse three-digit number.
# Take input
num=int(input("Enter a three-digit number:"))
# Reverse number
digit1=num//100
digit2=(num%100)//10
digit3=num%10
reversed_num=digit3*100+digit2*10+digit1
# Print reversed number
print(f"Reversed number of {num} is {reversed_num}.")
    