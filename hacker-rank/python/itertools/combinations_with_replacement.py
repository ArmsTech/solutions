# Itertools Combinations With Replacement
"""
You are given a string S.
Your task is to print all possible combinations with replacement of size k,
of the string in lexicographic sorted order.
"""

import itertools

string, size = raw_input().split()
size = int(size)
string = sorted(string)

for combination in itertools.combinations_with_replacement(string, size):
    print ''.join(combination)
