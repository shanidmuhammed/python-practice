# Provide an implementation for zip function using list comprehensions.

def zip_func(val1, val2):
    return [(val1[x],val2[y]) for x in range(len(val1)) for y in range(len(val2)) if (x == y)]

print(zip_func([1, 2, 3], [1, 2, 3]))