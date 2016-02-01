# Start And End Challenge
"""
You are given a string S.
Your task is to find the indices of the start and end of string k in S.
"""

import re

string, substring = raw_input(), raw_input()

matches = list(re.finditer('(?=({0}))'.format(substring), string))

if matches:
    print '\n'.join(
        [str((match.start(1), match.end(1) - 1)) for match in matches])
else:
    print '(-1, -1)'
