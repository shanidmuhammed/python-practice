# Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example 'eat', 'ate' and 'tea' are anagrams.

def find_freq(word):
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1
    return freq

def anagrams(values):
    freqs = []
    for val in values:
        freqs[val] = find_freq(val)
    for i in range(len(freqs)):
        for j in range(i, len(freqs)):
            if freqs[]

print(anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']))
