# -*- coding: utf-8 -*-
# Piling Up Challenge
"""
There is a horizontal row of n cubes. Side length of each cube from left to
right is given. You need to create a new vertical pile of cubes. The new pile
should be such that if cubei is on cubej then sideLengthj≥sideLengthi. But at
a time, you can only pick either the leftmost or the rightmost cube only.
Print "Yes" if its possible, "No" otherwise.
"""

from collections import deque


for _ in range(int(raw_input())):
    max_length = int(raw_input())
    deck = deque(map(int, raw_input().split()), max_length)

    last_length = -1
    passes_test = True

    for _ in range(len(deck) / 2):
        try:
            left_most = deck.popleft()
        except IndexError:
            left_most = -1

        try:
            right_most = deck.pop()
        except IndexError:
            right_most = -1

        if left_most >= last_length or right_most >= last_length:
            passes_test = False
            break

        last_length = left_most if left_most <= right_most else right_most

    print 'Yes' if passes_test else 'No'
