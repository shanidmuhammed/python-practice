# Write a function my_enumerate that works like enumerate.

def my_enumerate(values):
    index = 0
    for x in values:
        yield (index, x)
        index += 1

for i, c in my_enumerate(["a", "b", "c"]):
    print(i, c)