# Write a regular expression to validate a phone number.

import re

def validate(number):
    str_num = str(number)
    if len(str_num) < 7 or len(str_num) > 13:
        return "Not a phone number"
    return bool(re.fullmatch(r'\d+', str_num))

print(validate(1111))
