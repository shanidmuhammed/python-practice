# Improve the above program to print the words in the descending order of the number of occurrences.

def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

def read_words(filename):
    return open(filename).read().split()

def main(filename):
    frequency = word_frequency(read_words(filename))
    result = sorted(frequency, key = lambda x: frequency.get(x), reverse = True)
    for res in result:
        print(res, frequency.get(res))

if __name__ == "__main__":
    import sys
    main(sys.argv[1])