"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""



from string import punctuation


def pig_it(text):
    string = []
    for word in text.split():
        if word in punctuation:
            string.append(word)
        else:
            string.append(word[1:] + word[0] + 'ay')
    return ' '.join(string)