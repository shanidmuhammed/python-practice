# Write a python function parse_csv to parse csv (comma separated values) files.

def parse_csv(filename):
    result = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            result.append(line)
    return [x.split(',') for x in result]


print(parse_csv('test.csv'))