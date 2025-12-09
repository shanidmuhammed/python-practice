# Implement a function izip that works like itertools.izip.

def my_izip(values1, values2):
    it1 = iter(values1)
    it2 = iter(values2)
    for i in values1:
        if it2:
            yield (next(it1), next(it2))

for x, y in my_izip(["a", "b", "c"], [1, 2, 3]):
    print(x, y)