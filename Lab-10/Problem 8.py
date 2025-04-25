with open("Q8.txt", "r") as file:
    content = file.read()

print("Original Content:")
print(content)

words_to_replace = ["a", "the", "an"]

for word in words_to_replace:
    content = content.replace(word, " ")

print("\nModified Content:")
print(content)

with open("Q8_modified.txt", "w") as file:
    file.write(content)

print("\nModified content written to Q8_modified.txt")

with open("Q8_modified.txt", "r") as file:
    modified_content = file.read()

print("\nModified Content Read from Q8_modified.txt:")
print(modified_content)
