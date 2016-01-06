# Arrays Challenge
"""
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.
"""

import numpy

numbers = raw_input().split()
numbers.reverse()

print numpy.array(numbers, float)
