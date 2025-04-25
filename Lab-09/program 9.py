def count_alpha_digits(s):
    result = {'alphabets': 0, 'digits': 0}
    for char in s:
        if char.isalpha():
            result['alphabets'] += 1
        elif char.isdigit():
            result['digits'] += 1
    return result
a=input("enter a string")

print(count_alpha_digits(a))
