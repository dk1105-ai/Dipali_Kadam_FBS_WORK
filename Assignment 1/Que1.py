# Q.1  Write a program to calculate the percentage of student based on marks of any 5 subjects.

#Enter Marks of 5 subjects
math=int(input("Enter marks of Math:"))
science=int(input("Enter marks of Science:"))
english=int(input("Enter marks of English:"))
hindi=int(input("Enter marks of Hindi:"))
marathi=int(input("Enter marks of Marathi:"))

#Calculate total marks
total=math+science+english+hindi+marathi
#Calculate percentage
percentage=(total/500)*100
#Print percentage
print(f'Your Percentage is {percentage}%.')