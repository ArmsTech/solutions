# Check Strict Superset Challenge
"""
You are given a set A and N numbers of other sets.
Your job is to find whether set A is a strict superset of all the N sets.
Print True, if it is a strict superset of all N sets otherwise print False.
"""

set_ = set(raw_input().split())
supersets = []

for _ in range(int(raw_input())):
    other_set = set(raw_input().split())
    supersets.append(set_.issuperset(other_set))

print all(supersets)
