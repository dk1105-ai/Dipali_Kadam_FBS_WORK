# Q.5   Sum of all prime numbers between 1 to n
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input("Enter the value of n: "))

sum = 0
for i in range(1, num + 1):
    if is_prime(i):
        sum += i

print(f"The sum of all prime numbers between 1 and {num} is: {sum}")