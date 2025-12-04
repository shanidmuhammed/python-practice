# Write a function dups to find all duplicates in the list.

def dups(values):
    seen = set()
    result = []
    for val in values:
        if val not in seen:
            seen.add(val)
        else:
            result.append(val)
    return result

print(dups([1, 2, 1, 3, 2, 5]))