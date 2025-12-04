# Write a function unique to find all the unique elements of a list.

def unique(values):
    return {*values}

print(unique([1, 2, 1, 3, 2, 5]))