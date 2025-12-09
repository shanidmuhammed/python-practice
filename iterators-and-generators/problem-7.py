# Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

import sys

def split_file(n, filename):
    with open(filename) as f:
        for line in f.readlines():
            content = []
            for _ in range(n):
                content.append(line)
        yield [*content]

n = int(sys.argv[1])
filename = sys.argv[2]
result = split_file(n, filename)
for res in result:
    print(res)