# Loops Challenge
"""
Read an integer N. For all non-negative integers i<N, print i2. See the
sample for details.
"""

n = int(raw_input())

for number in range(0, n):
    print pow(number, 2)
