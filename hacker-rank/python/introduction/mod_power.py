# Mod Power Challenge
"""
You are given three integers; print two lines.
The first line should print pow(a,b), and the second line should print the
result of pow(a,b,m).
"""

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

print a ** b
print pow(a, b, c)
