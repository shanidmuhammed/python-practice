# Generalize the above implementation of csv parser to support any delimiter and comments.

def parse_csv(filename, delimiter, comment):
    content = []
    with open(filename) as f:
        for line in f:
            if comment in line:
                continue
            else:
                line = line.rstrip("\n")
                content.append(line)
    return [x.split(delimiter) for x in content]

print(parse_csv('test.csv', '!', '#'))