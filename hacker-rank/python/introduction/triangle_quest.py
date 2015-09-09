# Triangle Quest Challenge
"""
You are given a positive integer N. You have to print a numerical triangle of
height N−1.
"""
for number in range(1, input()):
    print number * (10 ** number - 1) / 9
