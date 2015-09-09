# Mod Divmod Challenge
"""
Read two integers, a and b, and print three lines.
The first line is the integer division a//b (Remember to
import division from __future__).
The second line is the result of a%b. (Modulo operator).
In the third line print the divmod of a and b.
"""

from __future__ import division

a = int(raw_input())
b = int(raw_input())

print a // b
print a % b
print divmod(a, b)
