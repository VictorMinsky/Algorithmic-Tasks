"""
Count how often sign changes in array.

result
number from 0 to ... . Empty array returns 0

example
const arr = [1, -3, -4, 0, 5]

| elem | count |
|------|-------|
|  1   |  0    |
| -3   |  1    |
| -4   |  1    |
|  0   |  2    |
|  5   |  2    |

return 2;
"""



def catch_sign_change(lst):
    if not lst:
        return 0
    sign = 0 if lst[0] < 0 else 1
    ans = 0
    for i in lst:
        if (0 if i < 0 else 1) == sign:
            continue
        else:
            ans += 1
            sign = 0 if sign == 1 else 1
    return ans
