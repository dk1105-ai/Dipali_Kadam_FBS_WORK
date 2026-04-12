# Q.2 pattern 


for i in range(1, 10):
    for j in range(1, 6):
        if (i <= 5 and j <= i) or (i > 5 and j <= 10 - i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()