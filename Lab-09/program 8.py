def convert(s):
    words = sorted(set(s.split()))
    return ' '.join(words)
str1=input("enter a string")

print(convert(str1))
