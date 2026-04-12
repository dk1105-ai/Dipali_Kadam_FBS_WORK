# Q.7 pattern 
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        print(chr(64 + k), end=" ")
    print()