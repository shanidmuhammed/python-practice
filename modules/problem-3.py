# Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.

import os

def list_files(dir_name):
    for file in os.listdir(dir_name):
        with open(file) as f:
            content = f.readlines()
        modified_time = os.stat(file).st_mtime
        length = os.stat(file).st_size
        print(f"File name: {file}, Length: {length}, Modified_time: {modified_time}")

dir = "/home/shanid-v-v/Desktop/python-practice/modules"
list_files(dir)