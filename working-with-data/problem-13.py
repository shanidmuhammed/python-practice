# Write a function lensort to sort a list of strings based on length.

def lensort(strs):
    strs.sort(key = lambda x: len(x))
    return strs

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))

