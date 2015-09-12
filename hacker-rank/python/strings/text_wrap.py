# Text Wrap Challenge
"""
You are given string S and width w.
Your task is to wrap the string into a paragraph of width w.
"""

import textwrap

string = raw_input()
width = int(raw_input())

print textwrap.fill(string, width)
