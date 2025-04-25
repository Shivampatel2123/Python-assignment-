def pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  
            for c in range(b, limit + 1):
                if a**2 + b**2 == c**2:
                    triplets.append((a, b, c))
    return triplets

limit = 30
triplets = pythagorean_triplets(limit)

print("Pythagorean triplets with side length <= 30:")
for triplet in triplets:
    print(triplet)
