# Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.

import os
import inspect
import importlib

def print_doc(mod_name):
    my_mod = importlib.import_module(mod_name)
    print(f"Help on module {mod_name}:")
    print("DESCRIPTION")
    print(my_mod.__doc__)
    members = inspect.getmembers(my_mod)
    print("FUNCTIONS:")
    for member in members:
        if inspect.isfunction(member[1]):
            print(member[0])
            print(member[1].__doc__)

print_doc('os')