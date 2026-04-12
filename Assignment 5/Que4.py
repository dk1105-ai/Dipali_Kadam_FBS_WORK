#Q 4. WAP to print Armstrong number within a given range
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    temp = num
    digits = len(str(num))   # number of digits
    sum = 0

    while temp > 0:
        rem = temp % 10
        sum += rem ** digits
        temp //= 10

    if sum == num:
        print(num)