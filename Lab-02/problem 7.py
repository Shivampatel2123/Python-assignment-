a=int(input("Enter the number: "))
if a%4==0 and a%400==0 and a%100!=0:
    print("leap year")
else:
    print("Not leap year")
