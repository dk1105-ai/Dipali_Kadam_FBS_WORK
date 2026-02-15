# Q.8. Write a program to swap two numbers using third variable.
# Take input
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
# Swap numbers using third variable
temp=num1
num1=num2
num2=temp
# Print swapped numbers
print(f"After swapping, first number is {num1} and second number is {num2}.")
