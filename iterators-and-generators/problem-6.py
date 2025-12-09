# Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.

import os

def num_code(dir_name):
    for entry in os.scandir(dir_name):
        if entry.is_dir():
            yield from num_code(entry.path)
        elif entry.is_file() and entry.name.endswith('.py'):
            with open(entry.path) as f:
                for line in f:
                    if line != '\n' and not line.startswith('#'):
                        yield 1
result = num_code('../functional-programming')
print(sum(result))
            
