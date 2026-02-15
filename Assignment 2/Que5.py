# Q.5 WAP to calculate selling price of book based on cost price and discount.
# Take input
cost_price=float(input("Enter cost price of book:"))
discount=float(input("Enter discount percentage:"))
#Calculate selling price
selling_price=cost_price-(cost_price*discount/100)
#Print selling price
print(f"Selling price of book is {selling_price}.")