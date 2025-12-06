# Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.

def invertdict(obj):
    result = {}
    for key, value in obj.items():
        result[value] = key
    return result

print(invertdict({'x': 1, 'y': 2, 'z': 3}))