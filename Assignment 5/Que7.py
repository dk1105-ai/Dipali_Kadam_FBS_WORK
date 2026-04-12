# Q.7  Write a program to solve the following series :  
# a. 1! + 2! + 3! + 4! + …..n!  
# b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)  
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.  
# d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10  
# e. x - x2/3 + x3/5 - x4/7 + …. to n terms 

# a. 1! + 2! + 3! + 4! + …..n!  
def factorial(num):
    count = 0
    fact = 1
    for i in range(1, num + 1):
        fact *= i
        count += fact
    return count
num = int(input("Enter the value of n: "))
print(f"The sum of the series 1! + 2! + 3! + ... + {num}! is: {factorial(num)}")

# b. N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)  
def power_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum += n ** i
    return sum  
n = int(input("Enter the value of n: "))
print(f"The sum of the series N + N^2 + N^3 + ... + N^{n} is: {power_series(n)}")

# c. Find the sum of a geometric series from 1 to n where the common ratio is 2. 
def geometric_series(n):
    sum = 0
    for i in range(n + 1):
        sum += 2 ** i
    return sum

n = int(input("Enter the value of n: "))
print(f"The sum of the geometric series from 1 to {n} with common ratio 2 is: {geometric_series(n)}")

# d. S = a + a2 / 2 + a3 / 3 + …… + a10 / 10  
def series_d(a):
    sum = 0
    for i in range(1, 11):
        sum += a ** i / i
    return sum
a = float(input("Enter the value of a: "))
print(f"The sum of the series S = a + a^2 / 2 + a^3 / 3 + ... + a^10 / 10 is: {series_d(a)}")

# e. x - x2/3 + x3/5 - x4/7 + …. to n terms
def sum_series_e(x, n):
    sum = 0
    for i in range(1, n + 1):
        term = x ** i / (2 * i - 1)
        if i % 2 == 0:
            sum -= term
        else:
            sum += term
    return sum
x = float(input("Enter the value of x: "))  
print(f"the series:{sum_series_e(x,n)}")

