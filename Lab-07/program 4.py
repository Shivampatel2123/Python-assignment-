
input_string = input("Enter a string: ")
char_frequency = {}
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print("Character frequency in the string:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")
