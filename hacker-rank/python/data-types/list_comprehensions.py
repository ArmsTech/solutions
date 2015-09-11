# List Comprehensions Challenge
"""
You are given three integers X, Y and Z denoting the dimensions of a Cuboid.
You have to print a list of all possible coordinates on the three dimensional
grid, such that at any point the sum Xi + Yi + Zi is not equal to N. If
X = 2, then possible values of Xi can be 0, 1 and 2. The same applies to Y
and Z.
"""

x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())

print [
    [x1, y1, z1]
    for x1 in range(x + 1)
    for y1 in range(y + 1)
    for z1 in range(z + 1)
    if x1 + y1 + z1 != n]
