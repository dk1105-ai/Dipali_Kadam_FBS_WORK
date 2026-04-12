# Q2. Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.
students = int(input("enter no of students:"))
total_percentage=0
for i in range(1,students+1):
    sub1=int(input("enter marks for sub1:"))
    sub2=int(input("enter marks for sub2:"))
    sub3=int(input("enter marks for sub3:"))
    sub4=int(input("enter marks for sub4:"))
    sub5=int(input("enter marks for sub5:"))
    total=sub1+sub2+sub3+sub4+sub5
    percentage=total/5
    total_percentage += percentage
    print(f"studennt {i}  percentage is {percentage}%")
avg=total_percentage/students
print(f"average percentage of class is {avg}%")
