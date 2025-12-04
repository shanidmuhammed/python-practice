# Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum.

a = [1, 2, 3]

def add(x):
   result = 0
   for i in range(0, len(x)):
    result += x[i]
   return result

print(add(a))