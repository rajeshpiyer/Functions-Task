def sortHyphenSeparatedSequence(a):
    words = a.split('-')
    words.sort()
    result = '-'.join(words)
    return result

a = input("Enter a hyphen-separated sequence of words: ")
result = sortHyphenSeparatedSequence(a)
print("Sorted sequence:", result)