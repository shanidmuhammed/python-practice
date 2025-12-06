# Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?

def char_freq(filename):
    content = ''
    freq = {}
    with open(filename) as f:
        for line in f:
            content += line
    for char in content:
            freq[char] = freq.get(char, 0) + 1
    return freq

result = char_freq('grep.txt')
for char in result:
        print(char, result.get(char))
        