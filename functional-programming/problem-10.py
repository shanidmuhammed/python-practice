# Write a function profile, which takes a function as argument and returns a new function, which behaves exactly similar to the given function, except that it prints the time consumed in executing it.

import time

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def profile(f):
    def g(value):
        f(value)
    return g

fib = profile(fib)
fib(20)