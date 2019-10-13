"""
You will be provided with 3 numbers: num1, num2 and a target number target. Your job is to write a program that will return the correct operator to get num1 and num2 to the target variable.

It can return either: add, subtract, multiply or divide appropriately.

If there are two answers, (2+2=4, 2*2=4), you can return either.

Note: the order of num1 and num2 is not mandatory:

get_op(3, 6, 2) = 'divide'      # because 6 / 3 = 2
get_op(1, 4, 3) = 'subtract'    # because 4 - 1 = 3
Range of random tests: -10000 <= num1, num2, target <= 10000
"""



def get_op(num1, num2, target):
    if num1 + num2 == target:
        return 'add'
    elif num1 - num2 == target or num2 - num1 == target:
        return 'subtract'
    elif num1 * num2 == target:
        return 'multiply'
    else:
        return 'divide'
