# Check Subset Challenge
"""
You are given two sets A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.
"""

answers = []

for _ in range(int(raw_input())):
    raw_input()  # Ignore this line
    set_ = set(raw_input().split())

    raw_input()  # Ignore this line
    other_set = set(raw_input().split())

    answers.append(set_.issubset(other_set))

for answer in answers:
    print answer
