# Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.

import os

def display_files(dir_name, i = None):
    i = 1 if i is None else i+1
    for entry in os.listdir(dir_name):
        path = os.path.join(dir_name, entry)
        print('|-- ', entry)
        if os.path.isdir(path):
            print('|   ' * i, end="")
            display_files(path, i)
            
dir_name = "../modules"
display_files(dir_name)