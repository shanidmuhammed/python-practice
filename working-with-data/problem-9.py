# Write a function cumulative_product to compute cumulative product of a list of numbers.

def cumulative_product(values):
    for i in range(1, len(values)):
        values[i] *= values[i-1]
    return values

print(cumulative_product([1, 2, 3, 4]))