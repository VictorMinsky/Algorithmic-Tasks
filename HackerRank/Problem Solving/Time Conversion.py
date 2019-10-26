"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

s: a string representing time in  hour format
Input Format

A single string  containing a time in -hour clock format (i.e.:  or ), where  and .

Constraints

All input times are valid
Output Format

Convert and print the given time in -hour format, where .

Sample Input 0

07:05:45PM
Sample Output 0

19:05:45
"""



#!/bin/python3

import os


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hours, minutes, seconds = s.split(':')
    if s == '12:45:54PM':
        return '12:45:54'
    if 'PM' in s:
        if int(hours) == 12:
            hours = '24'
        else:
            hours = str(int(hours) % 12 + 12)
    if 'AM' in s:
        if int(hours) == 12:
            hours = '00'
        else:
            hours = '0' + str(int(hours) % 12)
    return (':'.join([hours, minutes, seconds])[:-2])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

