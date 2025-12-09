# Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.

def peep(it):
   first, *rest = it
   return first, [first, *rest]

it = iter(range(5))
x, it1 = peep(it)
print(x, list(it1))