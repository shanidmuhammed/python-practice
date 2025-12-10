# Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

import sys

def split_file(n, filename):
    with open(filename) as f:
        for line in f:
            yield line

n = int(sys.argv[1])
filename = sys.argv[2]
result = split_file(n, filename)
j = 0
while(True):
    j += 1
    try:
        with open(f"file{j}.txt", 'w') as f:
            for i in range(n):
                f.write(next(result))
    except StopIteration:
        break