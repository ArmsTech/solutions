# Array Mathematics Challenge
"""
You are given two arrays (A & B) of dimensions NXM.
Your task is to perform the following operations:

  * Add (A + B)
  * Subtract (A - B)
  * Multiply (A * B)
  * Divide (A / B)
  * Mod (A % B)
  * Power (A ** B)
"""

import numpy

n, _ = map(int, raw_input().split())
arrays = []

for _ in range(2):
    array = []
    for _ in range(n):
        array.append(map(int, raw_input().split()))
    arrays.append(numpy.array(array))

a, b = arrays

print a + b
print a - b
print a * b
print a / b
print a % b
print a ** b
