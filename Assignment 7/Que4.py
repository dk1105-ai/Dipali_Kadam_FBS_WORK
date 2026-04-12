# Q.4 pattern
n = 5
for i in range(1, n+1):
    for s in range(n - i):
        print(" ", end=" ")
    
    # increasing
    for j in range(i, 2*i):
        print(j, end=" ")
    
    # decreasing
    for j in range(2*i - 2, i-1, -1):
        print(j, end=" ")
    
    print()