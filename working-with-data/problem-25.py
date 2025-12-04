# Provide an implementation for map using list comprehensions.

def square(x): return x * x

def map_func(func, values):
    return [func(x) for x in values]

print(map_func(square, range(5)))