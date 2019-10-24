"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""



def find_short(s):
    words = [(i, len(i)) for i in s.split()]
    return sorted(words, key=lambda x: x[1])[0][1]
