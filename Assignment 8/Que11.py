# Q.11  WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def armstrong(n):
    original = n
    sum_of_cubes = 0

    while n > 0:
        d = n % 10
        sum_of_cubes += d ** 3
        n = n // 10

    if original == sum_of_cubes:
        print("The number is an Armstrong number.")
    else:
        print("The number is not an Armstrong number.")

n = int(input("Enter number: "))
armstrong(n)