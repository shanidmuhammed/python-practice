# Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction.

class reverse_iter:
    def __init__(self, values):
        self.values = values

    def __iter__(self):
        return rev_iter_range(self.values)
    
class rev_iter_range:
    def __init__(self, values):
        self.i = len(values)
        self.values = values

    def __next__(self):
        if self.i > 0:
            self.i -= 1
            return self.values[self.i]
        else:
            raise StopIteration
        
rev = reverse_iter([1, 2, 3, 4, 5])

for i in rev:
    print(i)
