# Q.2 Write a program to calculate area of circle 
def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area
radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle is: {area_of_circle(radius)}")
