# Find The Maximum Depth Challenge
"""
You are given a valid XML document and you have to print the maximum level of
nesting in it. The first line of input is the number of XML lines followed by
the XML lines. Take the depth of root as 0.
"""

from xml.etree.ElementTree import XMLParser


class MaxDepthParser(object):

    """Find the maximum depth using a custom parses."""

    depth = 0
    max_depth = 0

    def start(self, tag, attrib):
        self.depth += 1
        if self.depth > self.max_depth:
            self.max_depth = self.depth

    def end(self, tag):
        self.depth -= 1

    def data(self, data):
        pass

    def close(self):
        return self.max_depth


xml_ = ''.join([raw_input() for _ in range(int(raw_input()))])

parser = XMLParser(target=MaxDepthParser())
parser.feed(xml_)
# -1 accounts for initial depth of 1
print parser.close() - 1
