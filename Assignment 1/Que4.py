# Q.4  Write a program to enter P, T, R and calculate simple Interest.

#Take input
P=int(input("Enter Principal amount:"))
T=int(input("Enter Time in years:"))
R=int(input("Enter Rate of Interest:"))

#Calculate Simple Interest
SI=(P*T*R)/100

#Print Simple Interest
print(f'Simple Interest is {SI}.')