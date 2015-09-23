# HTML Parser Part 1
"""
You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.

Format for printing the result is:

    Start : Tag1
    End   : Tag1
    Start : Tag2
    -> Attribute2[0] > Attribute_value2[0]
    -> Attribute2[1] > Attribute_value2[1]
    -> Attribute2[2] > Attribute_value2[2]
    Start : Tag3
    -> Attribute3[0] > None
    Empty : Tag4
    -> Attribute4[0] > Attribute_value4[0]
    End   : Tag3
    End   : Tag2

-> symbol indicates that tag contains an attribute. It is immediately
followed by the name of attribute and attribute value.
> symbol acts as a separator of attribute and attribute value.

If an HTML tag has no attribute then simply print the name of the tag.
If an attribute has no attribute value then simply print the name of
attribute value as None.

Note: Do not detect any HTML tag, attribute and attribute value, inside the
HTML comment tags (<!-- Comments -->).Comments can be multiline also.
"""

from HTMLParser import HTMLParser


class HackerRankParser(HTMLParser):

    """Parse HTML HackerRank provided tags."""

    def handle_starttag(self, tag, attributes):
        print "Start : %s" % tag
        for attribute in attributes:
            print "-> %s > %s" % attribute

    def handle_endtag(self, tag):
        print "End   : %s" % tag

    def handle_startendtag(self, tag, attributes):
        print "Empty : %s" % tag
        for attribute in attributes:
            print "-> %s > %s" % attribute

    def handle_comment(self, comment):
        pass


parser = HackerRankParser()
parser.feed(''.join([raw_input() for _ in range(int(raw_input()))]))
