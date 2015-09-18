# Itertools Product Challenge
"""
Your are given a two lists A and B. Your task is to compute Cartesian Product
AXB.
"""

import itertools

list_ = map(int, raw_input().split())
other_list = map(int, raw_input().split())

print ' '.join(map(str, list(itertools.product(list_, other_list))))
