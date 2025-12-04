# Write a function extsort to sort a list of files based on extension.

def extsort(values):
    values.sort(key = lambda x: (x.split('.'))[1])
    return values
    
print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))