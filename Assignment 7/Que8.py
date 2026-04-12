# Q.8 Pattern
k = 7

for i in range(1, 6):
    
    # left side (numbers)
    for j in range(1, i + 1):
        print(j, end=" ")
    
    # spaces
    for j in range(1, k + 1):
        print(" ", end=" ")
    k -= 2
    
    # right side (reverse numbers)
    for j in range(i, 0, -1):
        if i != 5 or j != i:   # avoid repeating middle number in last row
            print(j, end=" ")
    
    print()