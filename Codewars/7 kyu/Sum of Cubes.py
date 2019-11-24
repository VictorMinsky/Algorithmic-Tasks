"""
Write a function that takes a positive integer n, sums all the cubed values from 1 to n, and returns that sum.

Assume that the input n will always be a positive integer.

Examples:

sum_cubes(2)
> 9
# sum of the cubes of 1 and 2 is 1 + 8
"""



def sum_cubes(n):
    return sum([i ** 3 for i in range(1, n + 1)])
