# Transpose And Flatten Challenge
"""
You are given a NXM integer array matrix with space separated elements
(N = rows and M = columns). Your task is to print the transpose and flatten
results.
"""

import numpy

# We don't need columns
rows, _ = map(int, raw_input().split())

elements = numpy.array([map(int, raw_input().split()) for _ in range(rows)])

print numpy.transpose(elements)
print elements.flatten()
