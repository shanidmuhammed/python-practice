# What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.

a = ["aa", "bb", "cc"]

def add(values):
   result = ''
   for val in values:
    result += val
   return result

print(add(a))