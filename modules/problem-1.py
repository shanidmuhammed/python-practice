# Write a program to list all files in the given directory.

import os

current_path = "/src"

for file in os.listdir(current_path):
    print(file)