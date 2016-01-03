# Print Function Challenge
"""
Read an integer N. Without using any string methods, try to print the
following: 1,2,3.....N

Note that "....." represents the values in between.
"""

from __future__ import print_function

print(*range(1, int(raw_input()) + 1), sep='')
