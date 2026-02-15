# Q.3 Convert distance given in feet and inches into meter and centimeter.
# Take input
feet=int(input("Enter distance in feet:"))
inches=int(input("Enter distance in inches:"))
#Convert distance into meter
meter=(feet*0.3048)+(inches*0.0254)
#Convert distance into centimeter
centimeter=meter*100
#Print distance in meter and centimeter
print(f"Distance in meter is {meter}.")
print(f"Distance in centimeter is {centimeter}.")