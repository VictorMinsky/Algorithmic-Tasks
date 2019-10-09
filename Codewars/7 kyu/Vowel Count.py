"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.
"""



def getCount(inputStr):
    num_vowels = 0
    num_vowels = inputStr.count('a') + inputStr.count('e') + inputStr.count('i') + inputStr.count('o') + inputStr.count(
        'u')
    return num_vowels
