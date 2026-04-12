# Q.8 Write a program to check whether a number is prime or not using recursion.
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
       print(f"The {num} is prime number.")
def prime(num):
    return is_prime(num)
num=int(input("Enter the number:"))
prime(num)

    