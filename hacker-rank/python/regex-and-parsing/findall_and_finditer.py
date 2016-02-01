#  Findall and Finditer Challenge
"""
You are given a string S. It consists of alphanumeric characters, spaces and
symbols(+,-). Your task is to find all the substrings of S that contains 2 or
more vowels. Also, these substrings must lie in between 2 consonants and
should contain vowels only.
"""

import re

VOWELS = 'aeiou'
CONSONANTS = 'qwrtypsdfghjklzxcvbnm'

ALL_SUBSTRINGS_RE = re.compile(
    r'[%(consonants)s]([%(vowels)s]{2,})(?=[%(consonants)s])' % {
        'consonants': CONSONANTS, 'vowels': VOWELS}, flags=re.IGNORECASE)

substrings = ALL_SUBSTRINGS_RE.findall(raw_input())
print '\n'.join(substrings) if substrings else -1
