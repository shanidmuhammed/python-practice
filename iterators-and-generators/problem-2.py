#  Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.

def longer_lines(*filenames):
    for file in filenames:
        for f in open(file):
            if len(f) > 40:
                yield f

y = longer_lines('problem-1.py', 'hi.txt')

print(next(y))