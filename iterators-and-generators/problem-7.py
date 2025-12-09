# Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

import sys

def split_file(n, filename):
    n = int(n)
    with open(filename) as f:
        data = f.readlines()
        for line in data:
            content = []
            for i in range(n):
                content.append(line)
        yield content

n = sys.argv[1]
filename = sys.argv[2]
count = 0
result = split_file(n, filename)
for res in result:
#     count += 1
#     filename = f"file{count}.txt"
#     with open(filename, 'w') as f:
#         f.write(res)
        print(res)
