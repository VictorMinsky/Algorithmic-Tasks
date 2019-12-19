"""
Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.
"""



def find_longest(arr):
    return [i for i in arr if len(str(i)) == len(str(sorted(arr, key=lambda x: len(str(x)))[-1]))][0]
