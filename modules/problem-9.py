# Write a regular expression to validate a phone number.

import re

def validate(number):
    number = str(number)
    if len(number) < 7 or len(number) > 12:
        return "Not a phone number"
    result = re.fullmatch(r'\D', number)
    print(result)

print(validate(9834842459))
