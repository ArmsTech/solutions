# Itertools Combination Challenge
"""
You are given a string S.
Your task is to print all possible combinations upto size k, of the string in
lexicographic sorted order.
"""

import itertools

string, max_size = raw_input().split()
max_size = int(max_size)
string = sorted(string)

for size in range(1, max_size + 1):
    for combination in itertools.combinations(string, size):
        print ''.join(combination)
