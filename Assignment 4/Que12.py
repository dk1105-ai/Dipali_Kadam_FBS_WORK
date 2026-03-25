# Q12. Write a program to check if given number is Armstrong number or not.(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +4*4*4*4)
num=int(input("enter no:"))
sum=0
temp=num
order=len(str(num))
while(temp>0):
    digit=temp%10
    sum=sum+digit**order
    temp=temp//10
if(sum==num):
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")
    