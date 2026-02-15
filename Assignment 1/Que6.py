# Q.6  Write a Program to input two angles from user and find third angle of the triangle.

# take input
A=int(input("Enter first angle of triangle:"))
B=int(input("Enter second angle of triangle:"))
total=180


# calculate third angle
C=total-A-B

# print third angle
print(f'Third angle of triangle is {C}.')