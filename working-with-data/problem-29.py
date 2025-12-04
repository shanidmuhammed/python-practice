# Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:

def array(dim1, dim2):
    return [[None for x in range(dim2)] for x in range(dim1)]

print(array(2, 3))