# Zeros And Ones Challenge
"""
Your task is to print an array of size N and integer type using the tools
zeros and ones. N is the space separated list of the dimensions of the array.
"""

import numpy

dimensions = map(int, raw_input().split())

print numpy.zeros(dimensions, dtype=numpy.int)
print numpy.ones(dimensions, dtype=numpy.int)
