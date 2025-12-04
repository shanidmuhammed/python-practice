# Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?

def prod(values):
    result = 1
    for i in range(0, len(values)):
        result *= values[i]
    print(result)

def factorial(num):
    prod(list(range(1, num+1)))

factorial(4)