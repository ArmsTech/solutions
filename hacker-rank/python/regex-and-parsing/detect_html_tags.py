# Detect HTML Tags, Attributes And Attribute Values Challenge
"""
You are given an HTML code snippet of N lines.
Your task is to detect and print all HTML tags, attributes and attribute
values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]
-> symbol indicates that tag contains an attribute. It is immediately
   followed by the name of attribute and attribute value.
> symbol acts as a separator of attribute and attribute value.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute and attribute value, inside the
HTML comment tags (<!-- Comments -->).Comments can be multiline also.
All attributes have an attribute value.
"""

from HTMLParser import HTMLParser


class HackerRankParser(HTMLParser):

    """Parse HTML HackerRank provided tags."""

    def handle_starttag(self, tag, attributes):
        print tag
        for attribute in attributes:
            print "-> %s > %s" % attribute

    def handle_startendtag(self, tag, attributes):
        print tag
        for attribute in attributes:
            print "-> %s > %s" % attribute

    def handle_comment(self, comment):
        pass


parser = HackerRankParser()
parser.feed(''.join([raw_input() for _ in range(int(raw_input()))]))
