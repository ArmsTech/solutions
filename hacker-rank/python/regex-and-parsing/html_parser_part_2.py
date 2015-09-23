# -*- coding: utf-8 -*-
# HTML Parser Part 2
"""
You are given an HTML code snippet of N lines.
Your task is to print single−line comments, multi−line comments and data.

Format for printing the result is:

    >>> Single-line Comment
    Comment
    >>> Data
    My Data
    >>> Multi-line Comment
    Comment_multiline[0]
    Comment_multiline[1]
    >>> Data
    My Data
    >>> Single-line Comment:

Note : Do not print data if data == '\n'.
"""

from HTMLParser import HTMLParser


class HackerRankParser(HTMLParser):

    """Parse HTML HackerRank provided comments."""

    def handle_comment(self, comment):
        comment_type = 'Multi' if '\n' in comment else 'Single'
        print '>>> %s-line Comment' % comment_type
        print comment

    def handle_data(self, data):
        if data != '\r\n':
            print '>>> Data'
            print data


parser = HackerRankParser()
parser.feed('\n'.join([raw_input() for _ in range(int(raw_input()))]))
