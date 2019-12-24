"""
Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.
"""



import re


def is_digit(n):
    return True if re.fullmatch('[0-9]', n) else False
