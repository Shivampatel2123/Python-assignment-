a=int(input("Enter a first number:"))
b=int(input("Enter a second number:"))
n=int(input("Enter a number upto which we find a sum"))
c=0
print(a)
print(b)
for i in range(1,n-1):
    c=a+b
    b,a=c,b
    print(c)
    
    
