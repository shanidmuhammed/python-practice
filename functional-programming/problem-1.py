# Implement a function product to multiply 2 numbers recursively using + and - operators only.

def product(num1, num2):
    if num2 == 0:
        print(num1)
        return
    num1 = product(num1)