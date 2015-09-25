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

    last_stacked = None

    for _ in range(int(round(len(deck) / float(2)))):
        left_most = deck.popleft()

        try:
            right_most = deck.pop()
        except IndexError:
            passes_test = left_most <= last_stacked
            break

        first_to_stack = max(left_most, right_most)
        second_to_stack = min(left_most, right_most)

        passes_test = second_to_stack <= first_to_stack <= (
            last_stacked or first_to_stack)

        if not passes_test:
            break

        last_stacked = second_to_stack

    print 'Yes' if passes_test else 'No'
