# Write a function to compute the number of python files (.py extension) in a specified directory recursively.

import os

def num_py_files(dir_name):
    for entry in os.scandir(dir_name):
        if entry.is_dir() :
            yield from num_py_files(entry.path)
        elif entry.name.endswith('.py'):
            yield 1

result = num_py_files('../iterators-and-generators')
print(sum(result))