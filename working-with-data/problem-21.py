# Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.

import sys
filename = sys.argv[1]
width = int(sys.argv[2])

def wrap(filename, width):
    with open(filename) as f:
        for line in f:
            i = width
            while len(line) > width:
                print(line[:i])
                line = line[i:]
            print(line, end="")
            
wrap(filename, width)