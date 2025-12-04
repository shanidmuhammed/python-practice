# Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.

def head(file_name):
    with open(file_name) as f:
        data = f.readlines()
    for i in range(10):
        print(data[i])

def tail(file_name):
    with open(file_name) as f:
        data = f.readlines()
    for i in range(1,11):
        print(data[-i])

head('texts.txt')
tail('texts.txt')

