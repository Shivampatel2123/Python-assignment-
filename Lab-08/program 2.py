import random

randomnum = set()
while len(randomnum) < 10:
    randomnum.add(random.randint(15, 45))

count_less_than_30 = 0
for num in randomnum:
    if num < 30:
        count_less_than_30 += 1

filtered_numbers = set()
for num in randomnum:
    if num <= 35:
        filtered_numbers.add(num)

print("Random numbers after filtering:", filtered_numbers)
print("Count of numbers less than 30:", count_less_than_30)
