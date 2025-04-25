a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

print("Largest:", largest)
print("Smallest:", smallest)
