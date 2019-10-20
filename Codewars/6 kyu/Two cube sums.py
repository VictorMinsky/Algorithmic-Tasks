"""
Create a function

has_two_cube_sums(n)
which checks if a given number n can be written as the sum of two cubes in two different ways: n = a³+b³ = c³+d³. All the numbers a, b, c and d should be different and greater than 0.

E.g. 1729 = 9³+10³ = 1³+12³.

has_two_cube_sums(1729); // true
has_two_cube_sums(42);   // false
"""



def has_two_cube_sums(n):
    pairs = []
    for a in range(1, round(n ** (1 / 3)) + 2):
        for b in range(1, round(n ** (1 / 3)) + 2):
            if a ** 3 + b ** 3 == n:
                if sorted([a, b]) not in pairs:
                    pairs.append(sorted([a, b]))
    return True if len(pairs) >= 2 else False