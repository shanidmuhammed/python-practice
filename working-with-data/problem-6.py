# Write a function reverse to reverse a list. Can you do this without using list slicing?

def reverse(values):
    i = 0
    j = len(values) -1
    while(i < j):
        temp = values[i]
        values[i] = values[j]
        values[j] = temp
        i += 1
        j -= 1
    return values

print(reverse([1, 2, 3, 4]))