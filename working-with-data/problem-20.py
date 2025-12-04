# Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
# I'm sure that the shells are seashore shells.
# So if she sells seashells on the seashore,
# The shells that she sells areseashells I'm sure.
# She sells seashells on the seashore;

def grep(filename, word):
    with open(filename) as f:
        datas = f.readlines()
    for data in datas:
        if word in data:
            print(data, end="")

grep('grep.txt','sure')