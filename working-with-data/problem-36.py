# Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example 'eat', 'ate' and 'tea' are anagrams.

def find_freq(word):
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1
    return freq

def anagrams(values):
    result = []
    for i in range(len(values)):
        result[i] = values[i]
        for j in range(i, len(values)):
            if find_freq(values[i]) == find_freq(values[j]):
                result[i].append(values[j])
    return result


print(anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']))
