# Q.9 Write a program to swap two numbers without using third variable.
# Take input
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
# Swap numbers without using third variable
num1=num1+num2
num2=num1-num2
num1=num1-num2
# Print swapped numbers
print(f"After swapping, first number is {num1} and second number is {num2}.")