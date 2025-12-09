# Write a function vectorize which takes a function f and return a new function, which takes a list as argument and calls f for every element and returns the result as a list.

def vectorize(func):
    def g(values):
        result = []
        for val in values:
            result.append(func(val))
        return result
    return g

def square(x): return x * x

f = vectorize(square)
result = f([1, 2, 3])
print(result)

g = vectorize(len)
result = g([[1, 2], [2, 3, 4]])
print(result)

result = g([[1, 2], [2, 3, 4]])
print(result)