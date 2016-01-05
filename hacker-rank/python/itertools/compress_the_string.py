# Compress The String Challenge
"""
You are given a string S. Suppose a character 'c' occurs consecutively X
times in the string. Replace these consecutive occurrences of the character
'c' with (X,c) in the string.
"""

import itertools

string = raw_input()

compressed = []
for key, group in itertools.groupby(string):
    compressed.append((len(list(group)), int(key)))

print ' '.join(map(str, compressed))
