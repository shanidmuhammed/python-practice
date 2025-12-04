# Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.

def triplets(n):
    return [(i, j, i+j) for i in range(1, n) for j in range(i, n) if i+j < n]

print(triplets(5))