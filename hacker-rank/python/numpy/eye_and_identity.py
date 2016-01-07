# Eye And Identity Challenge
"""
Your task is to print an array of size NXM with its main diagonal elements as
1's and 0's everywhere else.
"""

import numpy

n, m = map(int, raw_input().split())

print numpy.eye(n, m)
