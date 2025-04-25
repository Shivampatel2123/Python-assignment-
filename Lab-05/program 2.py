import random
numbers = [random.randint(1, 20) for _ in range(20)]
print("Generated list:", numbers)
num = int(input("Enter a number to find: "))
positions = [i for i, x in enumerate(numbers) if x == num]
print("Occurrences at positions:", positions)
