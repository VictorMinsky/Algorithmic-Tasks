"""
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity
"""



def capitalize(s):
    ans = ['', '']
    for i in range(len(s)):
        if i % 2:
            ans[1] += s[i].upper()
            ans[0] += s[i].lower()
        else:
            ans[1] += s[i].lower()
            ans[0] += s[i].upper()
    return ans
