# Q. 1 Write a program to calculate area of rectangle
def area_of_rectangle(length, breadth):
    area = length * breadth
    return area
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
print(f"The area of the rectangle is: {area_of_rectangle(length, breadth)}")