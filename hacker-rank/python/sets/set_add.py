# Set Add Challenge
"""
Hari has a huge collection of country stamps. He decided to count total
number of distinct country stamps he has collected. He asked you to help him.
You pick stamps one by one from a stack of 'N' country stamps.

Your task is to find the total number of distinct country stamps.
"""

n = int(raw_input())
stamps = set([])

for _ in range(n):
    stamps.add(raw_input())

print len(stamps)
