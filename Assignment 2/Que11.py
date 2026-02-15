# Q.11. Write a program to accept an integer amount from user and tell minimumnumber of notes needed for representing that amount.
# Take input

amount=int(input("Enter an amount:"))
# Calculate minimum number of notes

notes_2000=amount//2000
amount=amount%2000

notes_500=amount//500
amount=amount%500

notes_200=amount//200
amount=amount%200

notes_100=amount//100
amount=amount%100

notes_50=amount//50
amount=amount%50

notes_20=amount//20
amount=amount%20

notes_10=amount//10
amount=amount%10

notes_5=amount//5
amount=amount%5

# Print minimum number of notes
print(f"Minimum number of notes needed for representing the amount is:")
print(f"2000: {notes_2000}")
print(f"500: {notes_500}")  
print(f"200: {notes_200}")
print(f"100: {notes_100}")
print(f"50: {notes_50}")
print(f"20: {notes_20}")
print(f"10: {notes_10}")
print(f"5: {notes_5}")
