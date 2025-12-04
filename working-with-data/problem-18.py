# Write a program to print each line of a file in reverse order.

def rev(f):
    lines = open(f).readlines()
    for line in lines:
        print(line[::-1])
        
rev('she.txt')