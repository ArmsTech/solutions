# RE Split Challenge
"""
You are given a string S, containing , and/or . and 0-9 digits.
Your task is to re.split() all of the , and . symbols.
"""

import re

COMMA_DOT_RE = re.compile('[,.]')

print '\n'.join([part for part in COMMA_DOT_RE.split(raw_input()) if part])
