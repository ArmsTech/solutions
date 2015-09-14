# Set Discard, Remove, Pop Challenge
"""
You have a non-empty set s and you have to execute N commands given in N
lines.

Commands will be pop, remove and discard.
"""

raw_input()
set_ = set(map(int, raw_input().split()))

n = int(raw_input())
for _ in range(n):
    line = raw_input().split()
    command = line.pop(0)
    arguments = map(int, line) if line else []

    if command == 'pop':
        set_.pop()
    else:
        getattr(set_, command)(*arguments)

print sum(set_)
