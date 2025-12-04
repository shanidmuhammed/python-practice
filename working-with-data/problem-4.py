# Implement a function product, to compute product of a list of numbers.

def prod(values):
    result = values[0]
    for i in range(1, len(values)):
        result *= values[i]
    print(result)

prod([2, 4, 5])