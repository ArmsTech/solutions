# Itertools Permutations Challenge
"""
You are given a string S.
Your task is to print all possible permutations of size k of the string in
lexicographic sorted order.
"""

import itertools

string, size = raw_input().split()
size = int(size)
string = sorted(string)

for permutation in itertools.permutations(string, size):
    print ''.join(permutation)
