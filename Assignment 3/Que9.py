# Q9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
math=float(input("Enter marks for math:"))
english=float(input("Enter marks for english:"))
science=float(input("Enter marks for science:"))
social=float(input("Enter marks for social:"))
hindi=float(input("Enter marks for hindi:"))
total=math+english+science+social+hindi
percentage=(total/500)*100
if(percentage>=86 and percentage<=100):
    print("Grade: First Class")
elif(percentage>=71 and percentage<86):
    print("Grade: Second Class")
elif(percentage>=55 and percentage<71):
    print("Grade: Third Class")
elif(percentage>=35 and percentage<54):
        print("Grade: Fourth Class")
elif(percentage>=0 and percentage<35):
     print("Grade: Fail")
else:
    print("Invalid percentage or Grade")