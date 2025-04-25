lst = ['madam', 'Python', 'malayalam', 12321]

def is_palindrome(word):
    return str(word) == str(word)[::-1]

for item in lst:
    if is_palindrome(item):  
        print(item)
