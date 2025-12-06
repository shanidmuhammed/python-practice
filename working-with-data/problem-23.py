# Write a program center_align.py to center align all lines in the given file.

import math

def center_align(filename):
    with open(filename) as f:
        content = f.readlines()
    max_size = max([len(x) for x in content])
    for line in content:
        diff = max_size - len(line)
        space_count = math.floor(diff/2)
        print(' '* space_count, line, end = "")

center_align('grep.txt')

