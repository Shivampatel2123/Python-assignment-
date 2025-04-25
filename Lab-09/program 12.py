def prime_factors(n, i=2):
    if n == 1:
        return []
    if n % i == 0:
        return [i] + prime_factors(n // i, i)
    return prime_factors(n, i + 1)


num = int(input("Enter a positive integer: "))
print("Prime Factors:", prime_factors(num))
