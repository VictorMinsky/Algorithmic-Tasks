"""
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are:

232
110011
54322345
Complete the function to test if the given number (num) can be rearranged to form a numerical palindrome or not. Return a boolean (true if it can be rearranged to a palindrome, and false if it cannot). Return "Not valid" if the input is not an integer or is less than 0.

For this kata, single digit numbers are NOT considered numerical palindromes.

Examples
5        =>  false
2121     =>  true
1331     =>  true
3357665  =>  true
1294     =>  false
"109982" =>  "Not valid"
-42      =>  "Not valid"
Other Kata in this Series:
Numerical Palindrome #1
Numerical Palindrome #1.5
Numerical Palindrome #2
Numerical Palindrome #3
Numerical Palindrome #3.5
Numerical Palindrome #4
Numerical Palindrome #5
"""



def palindrome(num):
    if not type(num) == int or num < 0:
        return 'Not valid'
    if num < 10:
        return False
    else:
        k = 0
        for i in str(num):
            if str(num).count(i) % 2:
                k += 1
        if k == 1 or not k:
            return True
        return False
