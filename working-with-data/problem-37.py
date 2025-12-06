# Write a function valuesort to sort values of a dictionary based on the key.

def valuesort(obj):
    return [obj[x] for x in sorted(obj, key = lambda x: x)]

print(valuesort({'x': 1, 'y': 2, 'a': 3}))