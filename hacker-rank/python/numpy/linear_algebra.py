# Linear Algebra Challenge
"""
You are given a square matrix A with dimensions NXN. Your task is to find the
determinant.
"""

import numpy

n = int(raw_input())
array = numpy.array([raw_input().split() for _ in range(n)], float)

print numpy.linalg.det(array)
