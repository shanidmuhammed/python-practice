# Write a function treemap to map a function over nested list.

def treemap(func, values, result=None):
    if result is None:
        result = []
    for val in values:
        if isinstance(val, list):
            treemap(func, val, result)
        else:
            result.append(func(val))
    return result

output = treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
print(output)