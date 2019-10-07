"""
Write function avg which calculates average of numbers in given list.

Python:

Due to rounding issues please do not use statistics.mean or such.
If the array is empty, return 0.
"""



def find_average(array):
    return 0 if len(array) == 0 else sum(array) / len(array)
