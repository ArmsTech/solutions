# Polar Coordinates Challenge
"""
You are given a complex z. Your task is to convert it to polar coordinate.
"""

import cmath

z = complex(raw_input())

print abs(z)
print cmath.phase(z)
