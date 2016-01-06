# Shape And Reshape Challenge
"""
You are given a space separated list of nine integers. Your task is to
convert this list into a 3X3 NumPy array.
"""

import numpy

integers = map(int, raw_input().split())
print numpy.reshape(integers, (3, 3))
