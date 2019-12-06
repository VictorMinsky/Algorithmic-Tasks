"""
You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has.

Input Format

The first line contains , the number of lines in the XML document.
The next  lines follow containing the XML document.

Output Format

Output a single line, the integer score of the given XML document.

Sample Input

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
Sample Output

5
Explanation

The feed and subtitle tag have one attribute each - lang.
The title and updated tags have no attributes.
The link tag has three attributes - rel, type and href.

So, the total score is .

There may be any level of nesting in the XML document. To learn about XML parsing, refer here.

NOTE: In order to parse and generate an XML element tree, use the following code:

>> import xml.etree.ElementTree as etree
>> tree = etree.ElementTree(etree.fromstring(xml))
Here, XML is the variable containing the string.
Also, to find the number of keys in a dictionary, use the len function:

>> dicti = {'0': 'This is zero', '1': 'This is one'}
>> print (len(dicti))

2
"""



import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    number_of_attributes = 0
    attrib = node.attrib
    number_of_attributes += len(attrib)
    for appt in node.getchildren():
        number_of_attributes += len(appt.attrib)
        for e in appt.getchildren():
            number_of_attributes += len(e.attrib)
    return number_of_attributes
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))