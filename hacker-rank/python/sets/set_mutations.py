# Set Mutations Challenge
"""
You are given a set A and N numbers of other sets. These N sets have to
perform some specific mutation operations to set A.

Your task is to execute those operations and print the sum of elements of
set A.
"""

raw_input()
set_ = set(map(int, raw_input().split()))

n = int(raw_input())
for _ in range(n):
    command = raw_input().split().pop(0)
    other_set = set(map(int, raw_input().split()))
    getattr(set_, command)(other_set)

print sum(set_)
