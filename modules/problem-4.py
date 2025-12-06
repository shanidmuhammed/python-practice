# Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.

import os

def display_files(dir_name):
    return os.listdir(dir_name)

dir_name = "/home/shanid-v-v/Desktop/python-practice/"
print(display_files(dir_name))