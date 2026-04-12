# Q.3 pattern 


for i in range(1, 6):
    for j in range(1, 6):
        if i == 5:  # last row
            print(j, end=" ")
        elif j == 1:  # first column
            print(1, end=" ")
        elif j == i:  # diagonal
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()