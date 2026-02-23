# Q6. Write a program to calculate profit or loss.
cost_price=float(input("Enter cost price: "))
selling_price=float(input("Enter selling price: "))
if (selling_price>cost_price):
    profit=selling_price-cost_price
    # profit%= (profit/cost_price)*100
    profit_per=(profit/cost_price)*100
    # print("The profit percentage is:",profit%)
    print("The profit percentage is:",profit_per)
elif (cost_price>selling_price):
    loss=cost_price-selling_price
    # loss%= (loss/cost_price)*100
    loss_per=(loss/cost_price)*100
    # print("The loss percentage is:",loss%)
    print("The loss percentage is:",loss_per)
else:
    print("No profit no loss.")