# The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?

def word_wrap(filename, width):
    with open(filename) as f:
        for line in f:
            i = width
            while len(line) > width:
                if line[(i-1)] != ' ':
                    i -= 1
                    continue
                print(line[:i])
                line = line[i:]
            print(line, end="")

word_wrap("grep.txt", 30)
