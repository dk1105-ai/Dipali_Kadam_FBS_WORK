# Q.3 3. Write a program to find sum of following series using functions : 
# a.  1+ 2 + 3 + 4+….. + n 
# b. 1!+ 2! + 3! + 4!+….. + n! 
# c. 1^1 + 2^2 + 3^3+ …… n^n
# for a. 1+ 2 + 3 + 4+….. + n 
def sum_of_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
n = int(input("Enter the value of n: "))
print(f"The sum of the series 1 + 2 + 3 + ... + {n} is: {sum_of_series(n)}")

# for b. 1!+ 2! + 3! + 4!+….. + n!
def factorial(num):
    count = 0
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        count += fact
    return count

num = int(input("Enter the value of n: "))
print(f"The sum of the series 1! + 2! + 3! + ... + {num}! is: {factorial(num)}")

# for c. 1^1 + 2^2 + 3^3+ …… n^n
def power_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** i
    return sum

n = int(input("Enter the value of n: "))
print(f"The sum of the series 1^1 + 2^2 + 3^3 + ... + {n}^{n} is: {power_series(n)}")