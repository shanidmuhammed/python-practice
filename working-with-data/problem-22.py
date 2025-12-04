# The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?

def word_wrap(filename, width):
    with open(filename) as f:
        for line in f:
            line = line.rstrip("\n")

            while len(line) > width:
                value = line[:width]
                if value == 
                line = line[width:]
            print(line)

word_wrap("grep.txt", 30)

# Incompleted