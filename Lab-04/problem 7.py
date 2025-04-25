import math  


n = int(input("Enter value for n: "))
r = int(input("Enter value for r: "))


npr = math.factorial(n) // math.factorial(n - r)
ncr = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


print(f"nPr ({n}P{r}) is: {npr}")
print(f"nCr ({n}C{r}) is: {ncr}")
