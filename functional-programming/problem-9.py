# Write a function permute to compute all possible permutations of elements of a given list.

def permute(values):
    return [[x, y, z] for x in values for y in values for z in values ]

print(permute([1, 2, 3]))