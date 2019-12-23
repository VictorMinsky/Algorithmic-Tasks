"""
Given a positive integer N, return the largest integer k such that 3^k < N.

For example,

largest_power(3) == 0
largest_power(4) == 1
You may assume that the input to your function is always a positive integer.
"""



def largest_power(N):
    ans = 0
    while 3 ** ans < N:
        ans += 1
    return ans - 1
