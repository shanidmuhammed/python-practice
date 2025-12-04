# Write a function group(list, size) that take a list and splits into smaller lists of given size.

def group(values, size):
    result = []
    i = 0
    j = size
    while i <= len(values):
        result.append(values[i:j])
        i , j = j, j + j
    return result

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
