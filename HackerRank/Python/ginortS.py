"""
You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324
"""



lower = []
upper = []
digits_odd = []
digits_even = []
for symbol in input():
    if symbol.islower():
        lower.append(symbol)
    elif symbol.isupper():
        upper.append(symbol)
    else:
        if int(symbol) % 2:
            digits_odd.append(symbol)
        else:
            digits_even.append(symbol)
print(''.join(sorted(lower) + sorted(upper) + sorted(digits_odd) + sorted(digits_even)))
