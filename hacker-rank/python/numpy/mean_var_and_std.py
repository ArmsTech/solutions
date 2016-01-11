# Mean, Var And Std Challenge
"""
The first line contains the space separated values of N and M.
The next N lines contains M space separated integers.
"""

import numpy

n, _ = map(int, raw_input().split())
array = numpy.array([raw_input().split() for _ in range(n)], float)

print numpy.mean(array, axis=1)
print numpy.var(array, axis=0)
print numpy.std(array)
