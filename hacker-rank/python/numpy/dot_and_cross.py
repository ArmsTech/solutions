# Dot And Cross Challenge
"""
You are given two arrays A and B. Both have dimensions of NXN.
Your task is to compute their matrix product.
"""

import numpy

n = int(raw_input())

array_a = numpy.array([raw_input().split() for _ in range(n)], int)
array_b = numpy.array([raw_input().split() for _ in range(n)], int)

print numpy.dot(array_a, array_b)
