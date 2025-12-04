# Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation for these functions.

def find_min(values):
    min_num = values[0]
    for val in values:
        if val < min_num:
            min_num = val
    return min_num

def find_max(values):
    max_num = values[0]
    for val in values:
        if val > max_num:
            max_num = val
    return max_num

print(find_min([1, 2, 3]))
print(find_max([1, 2, 3]))