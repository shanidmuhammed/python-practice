# Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.

import itertools

def peep(it):
   first = next(it)
   f_it = iter([first])
   return first, itertools.chain(f_it, it)
   
it = iter(range(5))
x, it1 = peep(it)
print(x, list(it1))