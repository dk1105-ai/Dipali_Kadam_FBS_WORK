# Q3.Accept no. of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition :a. Children below 12 = 30% discount b. Senior citizen (above 59) = 50% discount c. Others need to pay full.
num_passengers=int(input("enter number of passengers:"))
ticket_cost=int(input("enter per ticket cost:"))

total_amount=0
for i in range(num_passengers): 
    age=int(input(f"enter age of passenger {i+1}:"))
    if(age<12):
        total_amount=total_amount+(ticket_cost*0.7)
    elif(age>59):
        total_amount=total_amount+(ticket_cost*0.5)
    else:
        total_amount=total_amount+ticket_cost
print(f"total amount to ticket to travel for all passengers is {total_amount}.")
