# Provide an implementation for filter using list comprehensions.

def even(x): return x %2 == 0

def filter_func(func, values):
    return [x for x in values if func(x) == True]

print(filter_func(even, range(10)))

