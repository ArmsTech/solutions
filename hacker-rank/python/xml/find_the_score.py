# Find The Score Challenge
"""
You are given a valid XML document and you have to print its score. The first
line of input is the number of XML lines followed by the XML lines. Score is
given by the sum of score of each element. For any element, score is equal to
the number of attributes it has.
"""

import xml.etree.ElementTree as etree

xml_ = ''.join([raw_input() for _ in range(int(raw_input()))])
tree = etree.ElementTree(etree.fromstring(xml_))

print sum(
    map(len, [element.attrib for element in list(tree.getroot().iter())]))
