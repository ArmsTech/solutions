# Inner And Outer Challenge
"""
You are given two arrays: A and B.
Your task is to compute their inner and outer product.
"""

import numpy

array_a = numpy.array(raw_input().split(), int)
array_b = numpy.array(raw_input().split(), int)

print numpy.inner(array_a, array_b)
print numpy.outer(array_a, array_b)
