# -*- coding: utf-8 -*-
# No Idea Challenge
"""
There is an array of n integers, and 2 disjoint sets of m integers each A and
B. You like all integers in A and dislike all integers in B. Your initial
happiness is 0 and for each integer in the array, i, if i∈A, you add 1 to
your happiness, if i∈B, you add −1 to your happiness, else your happiness
does not change. Output your final happiness at the end.

Note that since A and B are sets, they have no repeated elements. But, the
array might contain duplicate elements.
"""

from collections import Counter

raw_input()  # Throw-away line

mood_data = map(int, raw_input().split())
happiness = 0
happy = set(map(int, raw_input().split()))
unhappy = set(map(int, raw_input().split()))

for mood, count in Counter(mood_data).iteritems():
    if mood in happy:
        happiness += 1 * count
    elif mood in unhappy:
        happiness -= 1 * count

print happiness
