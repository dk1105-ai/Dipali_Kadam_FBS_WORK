# Q.5 pattern 
n = 5

for i in range(1, n + 1):
    # spaces
    for j in range(n - i):
        print(" ", end=" ")

    # left side (always 1 for upper rows, full row for last)
    for j in range(1, i + 1):
        if i == n:
            print(j, end=" ")
        elif j == 1:
            print(1, end=" ")
        elif j == i:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    
    print()