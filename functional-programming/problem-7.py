# Implement a program dirtree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.

import os

def dirtree(dir_name, i = 0):
    for entry in os.listdir(dir_name):
        print('|   ' * i + '|-- ' + entry)
        path = os.path.join(dir_name, entry)
        if os.path.isdir(path):
            dirtree(path, i + 1)
dirtree('../functional-programming')