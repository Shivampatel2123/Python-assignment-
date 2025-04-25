x,y=5,5
radius=int(input("Enter radius of the circle"))
x1=int(input("Enter the x cordinate"))
y1=int(input("Enter the y cordinate"))
if (x-radius<x1<x+radius) and (y-radius<y1<y+radius):
    print("The point lies inside the circle")
else:
    print("The point lies outside the circle")
