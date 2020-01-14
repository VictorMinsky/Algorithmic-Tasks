"""
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples
divisors(4)  == 3  # 1, 2, 4
divisors(5)  == 2  # 1, 5
divisors(12) == 6  # 1, 2, 3, 4, 6, 12
divisors(30) == 8  # 1, 2, 3, 5, 6, 10, 15, 30
"""



def divisors(n):
    ans = 0
    for i in range(1, n + 1):
        if not n % i:
            ans += 1
    return ans
