# Q 8. Write a program to convert days into years, weeks and days.

#Take input
days=int(input("Enter number of days:"))
#Calculate years, weeks and days
years=days//365
weeks=(days%365)//7
remaining_days=(days%365)%7     

#Print years, weeks and days
print(f'{days} days is equal to {years} years, {weeks} weeks and {remaining_days} days.')