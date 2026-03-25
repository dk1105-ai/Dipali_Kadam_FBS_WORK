# Q9. 9. WAP to print all numbers in a range divisible by a given number.
start=int(input("enter start of range:"))
end=int(input("enter end of range:"))
divisor=int(input("enter divisor:"))
for i in range(start,end+1):
    if(i%divisor==0):
        print(i)