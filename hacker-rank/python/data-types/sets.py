# Sets Challenge
"""
You are given two set of integers M and N and you have to print their
symmetric difference in ascending order. The first line of input contains
value of M followed by M integers, then value of N followed by N integers.
Symmetric difference between M and N mean those values which either exist
in M or in N but not in both.
"""

raw_input()
m = set(map(int, raw_input().split()))
raw_input()
n = set(map(int, raw_input().split()))

# symmetric_difference = m.difference(n).union(n.difference(m))
for integer in sorted(list(m.symmetric_difference(n))):
    print integer
