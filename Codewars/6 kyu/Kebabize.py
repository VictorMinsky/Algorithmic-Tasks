"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
Notes:

the returned string should only contain lowercase letters
"""



def kebabize(string):
    string = string.translate(str.maketrans('0123456789', '          '))
    ans = []
    previous = 0
    current = 0
    for i in range(len(string)):
        if string[i].isupper():
            previous, current = current, i
            ans.append(string[previous:current].lower())
    ans.append(string[current:].lower())
    return '-'.join(ans).strip('- ').replace(' ', '')
