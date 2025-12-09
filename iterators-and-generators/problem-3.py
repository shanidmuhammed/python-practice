# Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

import os

def findfiles(dir_name):
    for file in os.listdir(dir_name):
        path = os.path.join(dir_name, file)
        if os.path.isdir(path):
            yield from findfiles(path)
        else:
            yield path

paths = findfiles('../functional-programming')
for path in paths:
    print(path) 