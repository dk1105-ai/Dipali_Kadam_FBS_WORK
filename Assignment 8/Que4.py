# Q.4 # Sum of all odd numbers between 1 to n 
def sum_of_odds(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            sum += i
    return sum

n = int(input("Enter the value of n: "))
print(f"The sum of all odd numbers between 1 and {n} is: {sum_of_odds(n)}")