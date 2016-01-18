# Any Or All Challenge
"""
You are given a space separated list of integers. If all the integers are
positive, then you need to check if any integer is a palindromic integer.
"""

_, integers = raw_input(), raw_input().split()
print all([int(integer) >= 0 for integer in integers]) and any(
    [integer == integer[::-1] for integer in integers])
