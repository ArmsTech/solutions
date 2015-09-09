# Interchange Two Numbers Challenge
"""
You are given two integers. Store them into two variables and exchange them.
Can it get any easier! Make sure you use tuple to do the task, rather than
using any fancy logic. Print the two numbers.
"""

a = int(raw_input())
b = int(raw_input())

a, b = b, a
print a
print b
