# Loops Challenge
"""
You have to initialize your list L = [] and follow the N commands given in
N lines.
"""

lines = int(raw_input())
list_ = []

for _ in range(0, lines):
    line = raw_input().split()
    command = line.pop(0)
    arguments = map(int, line) if line else []

    if command == 'print':
        print list_
    else:
        getattr(list_, command)(*arguments)
