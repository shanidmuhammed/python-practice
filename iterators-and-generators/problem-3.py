# Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

import os

current_dir = os.getcwd()

def findfiles(dir_name): 
    for file in os.listdir(dir_name):
        path = os.path.join(dir_name, file)
        if os.path.isdir(path):
            findfiles(path)
        else:
            yield os.path.abspath(path)

paths = findfiles('../../python-practice')
for path in paths:  
    print(path)