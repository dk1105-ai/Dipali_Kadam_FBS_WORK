# Q.6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

# Take input
basic=int(input("Enter basic salary of employee:"))
#Calculate da, ta, hra
da=0.1*basic
ta=0.12*basic
hra=0.15*basic
#Calculate total salary
total_salary=basic+da+ta+hra
#Print total salary

print(f"Total salary of employee is {total_salary}.")