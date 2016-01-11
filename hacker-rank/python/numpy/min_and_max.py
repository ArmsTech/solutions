# Min And Max Challenge
"""
The first line of input contains the space separated values of N and M.
The next N lines contains M space separated integers.
"""

import numpy

n, _ = map(int, raw_input().split())
array = numpy.array([raw_input().split() for _ in range(n)], int)

print numpy.max(numpy.min(array, axis=1))
