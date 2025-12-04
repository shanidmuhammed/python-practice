 # Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.

def enumerate(values):
    return [(x, values[x]) for x in range(len(values))]

print(enumerate(['a', 'b', 'c']))