# Concatenate Challenge
"""
You are given two integer arrays of size NXP and MXP (N & M are rows, and P
is the column). Your task is to concatenate the arrays along axis 0.
"""

import numpy

n_lines, m_lines, _ = map(int, raw_input().split())

n_elements = [
    numpy.array(map(int, raw_input().split())) for _ in range(n_lines)]
m_elements = [
    numpy.array(map(int, raw_input().split())) for _ in range(m_lines)]

print numpy.concatenate((n_elements, m_elements))
