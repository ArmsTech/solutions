# Polynomials Challenge
"""
You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.
"""

import numpy

coefficients = numpy.array(raw_input().split(), float)
value = int(raw_input())

print numpy.polyval(coefficients, value)
