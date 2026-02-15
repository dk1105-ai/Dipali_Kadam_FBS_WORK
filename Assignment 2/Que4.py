# Q.4 WAP to calculate area of triangle and rectangle
# Take input for triangle
base=int(input("Enter base of triangle:"))
height=int(input("Enter height of triangle:"))
#Calculate area of triangle
area_triangle=1/2*base*height
# Take input for rectangle
length=int(input("Enter length of rectangle:"))
breadth=int(input("Enter breadth of rectangle:"))
#Calculate area of rectangle
area_rectangle=length*breadth
#Print area of triangle and rectangle
print(f"Area of triangle is {area_triangle}.")
print(f"Area of rectangle is {area_rectangle}.")