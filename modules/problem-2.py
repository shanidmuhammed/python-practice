# Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.

import os

def extcount(dir_name):
    obj = {}
    files = os.listdir(dir_name)
    for file in files:
        ext = file.rsplit('.', 1)
        obj[ext[1]] = obj.get(ext[1], 0) + 1
    for key, value in obj.items():
        print(value, key)

dir = "/home/shanid-v-v/Desktop/python-practice/working-with-data"
extcount(dir)