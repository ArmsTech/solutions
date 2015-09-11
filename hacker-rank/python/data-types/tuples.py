# Tuples Challenge
"""
You are given an integer N in one line. The next line contains N
space-separated integers. Create a tuple of those N integers. Lets call it T.
Compute hash(T) and print it.
"""

raw_input()  # Not sure why we need to know how many integers :/
print hash(tuple(map(int, raw_input().split())))
