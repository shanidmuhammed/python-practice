# Write a function istrcmp to compare two strings, ignoring the case.
def istrcmp(str1, str2):
    return str1.upper() == str2.upper()

result = istrcmp('Python', 'python')
print(result)