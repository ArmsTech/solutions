# Deque Challenge
"""
Perform append, pop, popleft and appendleft methods on an empty deque d.
"""

from collections import deque

deck = deque()

for _ in range(int(raw_input())):
    operation = raw_input().split()

    if len(operation) == 1:
        getattr(deck, operation[0])()
    else:
        getattr(deck, operation[0])(operation[1])

print ' '.join(deck)
