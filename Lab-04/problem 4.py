def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

def armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    return sum_of_powers == num

def palindrome(num):
    return str(num) == str(num)[::-1]

def automorphic(num):
    square = num * num
    return str(square).endswith(str(num))

num = 191


print(f"Is {num} prime? {prime(num)}")
print(f"Is {num} perfect? {perfect(num)}")
print(f"Is {num} armstrong? {armstrong(num)}")
print(f"Is {num} palindrome? {palindrome(num)}")
print(f"Is {num} automorphic? {automorphic(num)}")
