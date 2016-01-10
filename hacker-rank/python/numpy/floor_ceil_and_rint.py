# Floor, Ceil, And Rint Challenge
"""
You are given a 1-D array, A. Your task is to print the floor, ceil and rint
of all the elements of A.
"""

import numpy

array = numpy.array(raw_input().split(), float)

print numpy.floor(array)
print numpy.ceil(array)
print numpy.rint(array)
