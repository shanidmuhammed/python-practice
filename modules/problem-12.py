import os
import inspect

def print_doc(mod_name):
    print(f"Help on module {mod_name}:")
    print("DESCRIPTION")
    print("FUNCTIONS:")
    for func in dir(os):
        if inspect.isfunction(func):
            print(func)

print_doc(os)