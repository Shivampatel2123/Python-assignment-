def frequency(s):
    words = s.split()
    freq_dict = {word: words.count(word) for word in sorted(set(words))}
    return freq_dict
a=input("enter words")

print(frequency(a))
