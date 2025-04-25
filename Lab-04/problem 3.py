str=input("Enter a string")
l=len(str)
c,n=0,0
for i in range(0,l):
    if str[i].isalpha() :
        c=c+1
    if str[i].isdigit() :
        n=n+1
print("character",c,"number",n)
        
    
    
