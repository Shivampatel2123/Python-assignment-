def ispalindrome(s):
    s = ''.join(s.lower().split())
    return s == s[::-1]
str1=input("enter a string")

print(ispalindrome(str1))
