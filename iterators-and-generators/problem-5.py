# Write a function to compute the total number of lines of code in all python files in the specified directory recursively.

import os

def num_lines(dir_name):
    files = os.listdir(dir_name)
    for file in files:
        path = os.path.join(dir_name, file)
        if os.path.isdir(path):
            yield from num_lines(path)
        else:
            if file.endswith('.py'):
                with open(path) as f:
                    content = f.readlines()
                    yield len(content)

result = num_lines('../../python-practice')
print(sum(result))