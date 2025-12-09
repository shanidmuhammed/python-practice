# Implement a function product to multiply 2 numbers recursively using + and - operators only.

def product(num1, num2):
    if num2 == 0: return 0
    else:
        return num1 + product(num1, num2-1)

print(product(22, 5))