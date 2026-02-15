# Q.5  Write a program to enter P, T, R and calculate Compound Interest.
#Take input
P=int(input("Enter Principal amount:"))
T=int(input("Enter Time in years:"))
R=int(input("Enter Rate of Interest:"))
#Calculate Compound Interest
CI=P*(1+R/100)**T-P
#Print Compound Interest
print(f'Compound Interest is {CI}.')