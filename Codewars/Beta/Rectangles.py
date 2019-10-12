"""
Rectangles
Write a function - called rectangle - that creates a rectangle using a specific character, with a specific width and height.

Newlines should be used for the height: \n

Your output cannot end with a newline.

Example
rectangle("*",5,3); /* =>
*****
*****
*****
*/
"""



def rectangle(char, width, height):
    ans = ''
    for y in range(height):
        ans += char * width + '\n'
    return ans[:-1]
