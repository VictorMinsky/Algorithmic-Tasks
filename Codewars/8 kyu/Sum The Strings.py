"""
Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

  sumStr("4", "5")    // should output "9"
  sumStr("34", "5")   // should output "39"
If either input is an empty string, consider it as zero.
"""



def sum_str(a, b):
    a = 0 if not a else int(a)
    b = 0 if not b else int(b)
    return str(a + b)
