import random
odd_numbers = random.sample(range(1, 100, 2), 5)
even_numbers = random.sample(range(2, 100, 2), 4)
print("odd numbers:", odd_numbers)
print("even numbers:", even_numbers)

odd_numbers[2] = even_numbers
print("Modified odd numbers:", odd_numbers)

flat_list = sorted([num for sublist in odd_numbers for num in (sublist if isinstance(sublist, list) else [sublist])])
print("Flattened and sorted list:", flat_list)
