"""
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""



def simple_multiplication(number):
    return number * 8 if not number % 2 else number * 9
